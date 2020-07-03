import paramiko


def sfcx(account, begin_date, end_date=''):
    # 开启SSH通道
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='10.0.134.110', port=22, username='hisusr', password='hisusr')

    stdin, stdout, stderr = ssh.exec_command(
        '. /dbhome/hisusr/.profile;sh /datatmp/sjm/YX_SFCX/sfcx.sh {account} {begin_date} {end_date}'
            .format(account=account, begin_date=begin_date, end_date=end_date))


def open_date_query(id_no='', org_no='', account=''):
    # 开启SSH通道
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='10.0.134.110', port=22, username='hisusr', password='hisusr')

    if id_no.strip():
        stdin, stdout, stderr = ssh.exec_command(
            '. /dbhome/hisusr/.profile;sh /datatmp/sjm/YX_SFCX/kh_zj_ds.sh {id_no}'
                .format(id_no=id_no))
    if org_no.strip():
        stdin, stdout, stderr = ssh.exec_command(
            '. /dbhome/hisusr/.profile;sh /datatmp/sjm/YX_SFCX/kh_zj_dg.sh {org_no}'
                .format(org_no=org_no))
    if account.strip():
        stdin, stdout, stderr = ssh.exec_command(
            '. /dbhome/hisusr/.profile;sh /datatmp/sjm/YX_SFCX/kh_zh.sh {account}'
                .format(account=account))
