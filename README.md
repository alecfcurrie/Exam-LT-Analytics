# Exam-LT-Analytics
A program for sythesizing data about learning technologies used in exams from exam info csvs.

## How to use

Make sure the exam spreadsheets are exported as CSVs. The input folder should include:

- 2022S1-2.csv
- 2022S1.csv
- 2022S2.csv
- 2022W1-2.csv
- 2022W1.csv
- 2022W2.csv
- 2023S1-2.csv
- 2023S1.csv
- 2023S2.csv
- 2023W1.csv

Make sure that the column headings for the appropriate columns are written exactly like this:

- MT LT
- MT Invig LT
- FE LT
- FE Invig LT

These headings are case-sensitive, and can not have trailing spaces.
## Computer Setup 
- Please have [VSCode](https://code.visualstudio.com/) and the [Python Extension](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) installed
- Have the following packages installed: [Pandas](https://pypi.org/project/pandas/)
- We recommend using the Rainbow CSV VSCode Extension for CSV readability (*optional*)

## Program Setup
1. [Clone this project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
 ```
git clone [add link once under scienceltrs repo]
```  
2. Replace the input the exam spreadsheets as CSVs in the input folder. This is the raw data
3. If **NEW** exam spreadsheets are added, make the following changes:
4. In path_names.py, add the new CSV(s) as follows
   ```
   path_yearTerm = 'input/filename.csv
   path_yearTerm = os,path.abspath(path_yearTerm)
   mt_yearTerm_path = 'output/mt_yearTerm_output.csv'
   mt_yearTerm_path = os.path.abspath(mt_yearTerm_path)
   fe_yearTerm_path = 'output/fe_yearTerm_output.csv'
   fe_yearTerm_path = os.path.abspath(fe_yearTerm_path)
   ```
5. In collect_data.py, add the output and input paths following the same format in:
   ```
   dataSetMT
   dataSetFet 
    ```
## Acknowledgments

The file pathNames was also taken from [SciPub Repository](https://github.com/scienceltrs/SciPub/blob/main/pathNames.py) and was modified for this project.

