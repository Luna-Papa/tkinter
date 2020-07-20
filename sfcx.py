import paramiko


def sfcx(account, begin_date, end_date=''):
    # 开启SSH通道
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='10.0.134.110', port=22, username='hisusr', password='hisusr')
    # ssh.connect(hostname='192.168.57.128', port=22, username='db2inst1', password='db2inst1')

    stdin, stdout, stderr = ssh.exec_command(
        '. /dbhome/hisusr/.profile;sh /datatmp/sjm/YX_SFCX/cx.sh {account} {begin_date} {end_date}'
            .format(account=account, begin_date=begin_date, end_date=end_date))


def open_date_query(id_no='', org_no='', account='', name=''):
    # 开启SSH通道
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(hostname='10.0.134.110', port=22, username='hisusr', password='hisusr')
    ssh.connect(hostname='192.168.57.128', port=22, username='db2inst1', password='db2inst1')


    if id_no:
        stdin, stdout, stderr = ssh.exec_command(
            '. /dbhome/hisusr/.profile;sh /datatmp/sjm/YX_SFCX/kh_zj_ds.sh {id_no}'
                .format(id_no=id_no))
    if org_no:
        stdin, stdout, stderr = ssh.exec_command(
            '. /dbhome/hisusr/.profile;sh /datatmp/sjm/YX_SFCX/kh_zj_dg.sh {org_no}'
                .format(org_no=org_no))
    if account:
        stdin, stdout, stderr = ssh.exec_command(
            '. /dbhome/hisusr/.profile;sh /datatmp/sjm/YX_SFCX/kh_zh.sh {account}'
                .format(account=account))
    if name:
        stdin, stdout, stderr = ssh.exec_command(
            'echo {name} > {name}.txt'.format(name=name))
        # stdin, stdout, stderr = ssh.exec_command(
        #     '. /dbhome/hisusr/.profile;sh /datatmp/sjm/YX_SFCX/kh_mc_dg.sh {name}'
        #         .format(name=name))


def pos_query(account, date, amt):
    # 开启SSH通道
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='10.0.134.110', port=22, username='hisusr', password='hisusr')

    stdin, stdout, stderr = ssh.exec_command(
        '. /dbhome/hisusr/.profile;sh /datatmp/sjm/YX_SFCX/pos.sh {account} {date} {amt}'
            .format(account=account, date=date, amt=amt))
