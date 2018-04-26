from django.contrib.auth import authenticate


class UserShell(object):
    """
    用户登录堡垒机后的shell操作
    """
    def __int__(self, sys_argv):
        self.sys_argv = sys_argv
        self.user = None

    def auth(self):
        """
        用户账户登录
        :return: 返回登录结果
        """
        count = 0
        while count < 3:
            username = input('username:').strip()
            password = input('password:').strip()
            user = authenticate(username=username,password=password)
            # None代表认证不成功
            # user object 认证对象
            if not user:
                count += 1
                print('用户名或密码错误！！！')
            else:
                self.user = user
                return True
        else:
            print('Too many attempts...')

    def start(self):
        """
        启动交互程序
        :return:
        """
        if self.auth():
            while True:
                host_groups = self.user.account.host_groups.all()
                for index,group in enumerate(host_groups):
                    print("%s.\t%s[%s]" % (index, group, group.host_user_binds.count()))
                print("%s.\t未分组机器[%s]" % (len(host_groups), self.user.account.host_user_binds.count()))

                choice1 = input("select group>:").strip()
                if choice1.isdigit():
                    choice1 = int(choice1)
                    host_bind_list = None
                    if choice1 >= 0 and choice1 < len(host_groups):
                        selected_group = host_groups[choice1]
                        host_bind_list = selected_group.host_user_binds.all()
                    elif choice1 == len(host_groups):  # 选择的未分组机器
                        # selected_group = self.user.account.host_user_binds.all()
                        host_bind_list = self.user.account.host_user_binds.all()
                    if host_bind_list:
                        while True:
                            for index, host in enumerate(host_bind_list):
                                print("%s.\t%s" % (index, host,))
                            choice2 = input("select host>:").strip()
                            if choice2.isdigit():
                                choice2 = int(choice2)
                                if choice2 >= 0 and choice2 < len(host_bind_list):
                                    selected_host = host_bind_list[choice2]
                                    print("selected host", selected_host)
                            elif choice2 == 'q' or choice2 == 'Q':
                                break
                            else:
                                print('input error')
                elif choice1 == 'q' or choice1 == 'Q':
                    break
                else:
                    print('input error')
