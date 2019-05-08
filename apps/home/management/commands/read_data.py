from django.core.management.base import BaseCommand
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

import ezodf
from django.conf import settings
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from home.models import University, Department, Year, DepName


class Command(BaseCommand):
    help = 'Create random users'

    def handle(self, *args, **kwargs):


         df = pd.read_excel('LisansDeparmanlarİçin - Kopya.xlsx', sheetname='Sheet1')

         print("Column headings:")
         print(df.columns)
         for i in df.index:
             print(df['programKısalmıs'][i])
             department_name, created = DepName.objects.get_or_create(department_name=df['programK'][i])

        # filename = '\LisansDeparmanlarİçin - Kopya.ods'
        # doc = ezodf.opendoc(settings.BASE_DIR + filename)
        #
        # print("Spreadsheet contains %d sheet(s)." % len(doc.sheets))
        # for sheet in doc.sheets:
        #     print("-" * 40)
        #     print("   Sheet name : '%s'" % sheet.name)
        #     print("Size of Sheet : (rows=%d, cols=%d)" % (sheet.nrows(), sheet.ncols()))
        #
        # # convert the first sheet to a pandas.DataFrame
        # sheet = doc.sheets[0]
        # df_dict = {}
        #
        # for i, row in enumerate(sheet.rows()):
        #     # row is a list of cells
        #     # assume the header is on the first row
        #     if i == 0:
        #         # columns as lists in a dictionary
        #         df_dict = {cell.value: [] for cell in row}
        #         # create index for the column headers
        #         col_index = {j: cell.value for j, cell in enumerate(row)}
        #         continue
        #     for j, cell in enumerate(row):
        #         # use header instead of column index
        #         df_dict[col_index[j]].append(cell.value)
        # # and convert to a DataFrame
        # df = pd.DataFrame(df_dict)
        # df.transpose()
        # print(df)
        #
        # for index, row in df.iterrows():
        #     print(index)
        #     department_name,created = DepName.objects.get_or_create(department_name=row['programKısalmıs'])

            # uni, created = University.objects.get_or_create(name=row['universite'])
            #
            # dep, created = Department.objects.get_or_create(
            #     dep_no=row['no'],
            #     defaults={
            #         'university': uni,
            #         'schoolarshipORgovernment': row['burs'],
            #         'pointType': row['puanTuru'],
            #         'dep_name': row['program']
            #     }
            # )
            #
            # years_dict = [
            #     [2015, 'kontenjan2015', 'tbs2015', 'tabanPuan2015'],
            #     [2016, 'kontenjan2016', 'tbs2016', 'tabanPuan2016'],
            #     [2017, 'kontenjan2017', 'tbs2017', 'tabanPuan2017'],
            #     [2018, 'kontenjan2018', 'tbs2018', 'tabanPuan2018']
            # ]
            #
            # for year in years_dict:
            #
            #     min_rank = row[year[2]]
            #     if min_rank == '---' or min_rank == 'Dolmadı' or min_rank == 'null':
            #         min_rank = '0'
            #
            #     min_point = row[year[3]]
            #     if min_point == '---' or min_point == 'Dolmadı' or min_point == '\'Dolmadı' or min_point == 'null':
            #         min_point = '0'
            #     else:
            #         min_point = min_point.replace(',', '.')
            #
            #     dep_cap = row[year[1]]
            #     dep_cap = dep_cap.split(' ', 1)[0]
            #     if dep_cap == 'null' or dep_cap == '---':
            #         dep_cap = '0'
            #
            #     Year.objects.get_or_create(
            #         department=dep,
            #         year=year[0],
            #         defaults={
            #             'dep_cap': int(dep_cap),
            #             'min_rank': int(min_rank),
            #             'min_point': float(min_point)
            #         }
            #     )
