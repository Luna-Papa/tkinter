from excel_magic.dataset import open_file
from sfcx import sfcx, open_date_query, pos_query
import time


def sfcx_batch_query(filename):
    with open_file(filename) as f:
        rows = f.get_sheet_by_index(0).get_rows()
        for row in rows:
            account = row['账号']
            begindate = row['起始日期']
            enddate = row['结束日期']
            sfcx(account, begindate, enddate)
            time.sleep(30)

