# -*- coding: utf-8 -*-
"""EDA_somin의 사본

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NpdCOhJ27JH8HDQLHErt9XI4Om45N3GA
"""
import glob
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import os
import seaborn as sns

"""# mid

### 모든 mid에 대한 파일명 - 파일경로
"""



# kinect_color 경로
kinect_color_path = r'C:\Final_project\data\activities_3s\kinect_color'

# mid로 시작하는 모든 파일 탐색
files_path = glob.glob(os.path.join(kinect_color_path, 'mid*'))
filtered_files_path = [file for file in files_path if not file.endswith('midlevel.chunks_90.csv')]

# mid 딕셔너리 생성
mid_dict = {}
for file_path in filtered_files_path:
  file_name = os.path.basename(file_path) # 파일 경로에서 파일 이름만 추출
  key = file_name.split("split_")[-1].replace('.csv', '')
  mid_dict[key] = file_path

df = pd.DataFrame(mid_dict.items(), columns = ['파일명', '파일경로'])
df['파일명'] = 'mid_' + df['파일명']
# print(df.to_markdown())

"""|    | 파일명      | 파일경로                                                                                                                       |
|---:|:------------|:-------------------------------------------------------------------------------------------------------------------------------|
|  0 | mid_1.val   | C:\Final_project\data\activities_3s\kinect_color/midlevel.chunks_90.split_1.val.csv   |
|  1 | mid_2.train | C:\Final_project\data\activities_3s\kinect_color/midlevel.chunks_90.split_2.train.csv |
|  2 | mid_2.test  | C:\Final_project\data\activities_3s\kinect_color/midlevel.chunks_90.split_2.test.csv  |
|  3 | mid_1.test  | C:\Final_project\data\activities_3s\kinect_color/midlevel.chunks_90.split_1.test.csv  |
|  4 | mid_0.train | C:\Final_project\data\activities_3s\kinect_color/midlevel.chunks_90.split_0.train.csv |
|  5 | mid_0.test  | C:\Final_project\data\activities_3s\kinect_color/midlevel.chunks_90.split_0.test.csv  |
|  6 | mid_1.train | C:\Final_project\data\activities_3s\kinect_color/midlevel.chunks_90.split_1.train.csv |
|  7 | mid_2.val   | C:\Final_project\data\activities_3s\kinect_color/midlevel.chunks_90.split_2.val.csv   |
|  8 | mid_0.val   | C:\Final_project\data\activities_3s\kinect_color/midlevel.chunks_90.split_0.val.csv   |

### total_mid 파일 head
"""

mid_path = 'C:\Final_project\data\activities_3s\kinect_color/midlevel.chunks_90.csv'
df_mid = pd.read_csv(mid_path) # df = dataframe
print(df_mid.head())

"""### total_mid 동영상 목록"""

mid_file_ids = df_mid['file_id'].unique()
# print('file_ids : \n', mid_file_ids)
df = DataFrame(mid_file_ids, columns = ['total_mid_file_ids'])
# print(df.to_markdown())

"""|    | total_mid_file_ids                         |
|---:|:-------------------------------------------|
|  0 | vp1/run1b_2018-05-29-14-02-47.kinect_color |
|  1 | vp1/run2_2018-05-29-14-33-44.kinect_color  |
|  2 | vp2/run1_2018-05-03-14-08-31.kinect_color  |
|  3 | vp2/run2_2018-05-24-17-22-26.kinect_color  |
|  4 | vp3/run1b_2018-05-08-08-46-01.kinect_color |
|  5 | vp3/run2_2018-05-29-16-03-37.kinect_color  |
|  6 | vp4/run1_2018-05-22-13-28-51.kinect_color  |
|  7 | vp4/run2_2018-05-22-14-25-04.kinect_color  |
|  8 | vp5/run1_2018-05-22-15-10-41.kinect_color  |
|  9 | vp5/run2b_2018-05-22-15-50-07.kinect_color |
| 10 | vp6/run1_2018-05-23-10-21-45.kinect_color  |
| 11 | vp6/run2_2018-05-23-11-05-00.kinect_color  |
| 12 | vp7/run1_2018-05-23-13-16-52.kinect_color  |
| 13 | vp7/run2b_2018-05-23-13-54-07.kinect_color |
| 14 | vp8/run1d_2018-05-23-14-54-38.kinect_color |
| 15 | vp8/run2_2018-05-23-15-30-27.kinect_color  |
| 16 | vp9/run1b_2018-05-23-16-19-17.kinect_color |
| 17 | vp10/run1_2018-05-24-13-14-41.kinect_color |
| 18 | vp10/run2_2018-05-24-14-08-46.kinect_color |
| 19 | vp11/run1_2018-05-24-13-44-01.kinect_color |
| 20 | vp11/run2_2018-05-24-14-35-56.kinect_color |
| 21 | vp12/run1_2018-05-24-15-44-28.kinect_color |
| 22 | vp12/run2_2018-05-24-16-21-35.kinect_color |
| 23 | vp13/run1_2018-05-29-15-21-10.kinect_color |
| 24 | vp13/run2_2018-05-30-11-34-54.kinect_color |
| 25 | vp14/run1_2018-05-30-10-11-09.kinect_color |
| 26 | vp14/run2_2018-05-30-10-42-33.kinect_color |
| 27 | vp15/run1_2018-05-30-13-05-35.kinect_color |
| 28 | vp15/run2_2018-05-30-13-34-33.kinect_color |

### total_mid activity에 대한 count
"""

df = pd.read_csv(mid_path)
activity_counts = df.groupby(['activity']).size().reset_index(name='count')

# print(activity_counts.to_markdown())

"""|    | activity                                  |   count |
|---:|:------------------------------------------|--------:|
|  0 | closing_backpack                          |      11 |
|  1 | closing_bottle                            |      98 |
|  2 | closing_door_inside                       |      30 |
|  3 | closing_door_outside                      |      22 |
|  4 | closing_laptop                            |      40 |
|  5 | drinking                                  |     159 |
|  6 | eating                                    |     877 |
|  7 | entering_car                              |      41 |
|  8 | exiting_car                               |      43 |
|  9 | fastening_seat_belt                       |     159 |
| 10 | fetching_an_object                        |     756 |
| 11 | interacting_with_phone                    |     471 |
| 12 | looking_back_left_shoulder                |      17 |
| 13 | looking_back_right_shoulder               |       1 |
| 14 | looking_or_moving_around (e.g. searching) |     102 |
| 15 | moving_towards_door                       |       7 |
| 16 | opening_backpack                          |      27 |
| 17 | opening_bottle                            |     119 |
| 18 | opening_door_inside                       |      39 |
| 19 | opening_door_outside                      |      30 |
| 20 | opening_laptop                            |      56 |
| 21 | placing_an_object                         |     688 |
| 22 | preparing_food                            |      61 |
| 23 | pressing_automation_button                |     272 |
| 24 | putting_laptop_into_backpack              |      26 |
| 25 | putting_on_jacket                         |     234 |
| 26 | putting_on_sunglasses                     |      74 |
| 27 | reading_magazine                          |     661 |
| 28 | reading_newspaper                         |     580 |
| 29 | sitting_still                             |    2797 |
| 30 | standing_by_the_door                      |       3 |
| 31 | taking_laptop_from_backpack               |      19 |
| 32 | taking_off_jacket                         |     138 |
| 33 | taking_off_sunglasses                     |      66 |
| 34 | talking_on_phone                          |     359 |
| 35 | unfastening_seat_belt                     |      89 |
| 36 | using_multimedia_display                  |     474 |
| 37 | working_on_laptop                         |     392 |
| 38 | writing                                   |     295 |

### activity에 대한 count 막대그래프
"""

def plot_activity_counts(mid_path):
    df = pd.read_csv(mid_path)

    activity_counts = df.groupby(['activity']).size().reset_index(name='count')
    activity_counts = activity_counts.sort_values(by='count', ascending=True) # count 기준 오름차순 정렬

    plt.figure(figsize=(10, 8))
    plt.barh(activity_counts['activity'], activity_counts['count'], alpha=0.8)
    plt.title(f"Activity Counts for {os.path.basename(mid_path)}", fontsize=14)
    plt.xlabel('Count', fontsize=12)
    plt.ylabel('Activity', fontsize=12)
    plt.yticks(fontsize=10)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()  # 레이아웃 자동 조정
    plt.show()

plot_activity_counts(mid_path)

"""### total_mid annotation_id 이상치"""

def annotation_id_sensor(mid_path):
    """
    주어진 파일 경로(mid_path)를 따라 데이터를 읽어,
    같은 activity가 연속되더라도 annotation_id가 다를 때를 감지하여
    file_id를 키로 하고, 이전 및 이후 frame_start, frame_end, activity를 값으로 하는 딕셔너리를 반환.

    Args:
    - mid_path (str): 처리할 파일의 경로

    Returns:
    - dict: key는 file_id, value는 {prev_frame_start, prev_frame_end, current_frame_start, current_frame_end, activity}인 딕셔너리
    """
    # 파일 읽기
    try:
        df = pd.read_csv(mid_path)

        # 데이터프레임 칼럼 확인
        required_columns = {'file_id', 'activity', 'annotation_id', 'frame_start', 'frame_end'}
        if not required_columns.issubset(df.columns):
            print(f"파일에 필요한 칼럼이 없습니다. (필요한 칼럼: {required_columns})")
            return {}

        # 같은 activity가 연속되더라도 annotation_id가 다를 때 감지
        result = {}
        prev_activity = None
        prev_annotation_id = None
        prev_frame_start = None
        prev_frame_end = None

        for _, row in df.iterrows():
            current_activity = row['activity']
            current_annotation_id = row['annotation_id']
            current_file_id = row['file_id']
            current_frame_start = row['frame_start']
            current_frame_end = row['frame_end']

            # annotation_id가 바뀌기 직전 행 감지
            if prev_activity == current_activity and current_annotation_id != prev_annotation_id:
                result[current_file_id] = {
                    'prev_frame_start': prev_frame_start,
                    'prev_frame_end': prev_frame_end,
                    'current_frame_start': current_frame_start,
                    'current_frame_end': current_frame_end,
                    'activity': prev_activity
                }

            # 이전 행 정보 업데이트
            prev_activity = current_activity
            prev_annotation_id = current_annotation_id
            prev_frame_start = current_frame_start
            prev_frame_end = current_frame_end

        return result

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")
        return {}

# 예시 실행
mid_path = '/content/drive/MyDrive/sesac_final_project_dataset/annotations/activities_3s/kinect_color/midlevel.chunks_90.csv'
result = annotation_id_sensor(mid_path)

def dict_to_markdown(result):
    """
    딕셔너리를 Markdown 형식의 표로 변환하여 출력합니다.

    Args:
    - result (dict): key가 file_id, value가 {prev_frame_start, prev_frame_end, current_frame_start, current_frame_end, activity}인 딕셔너리
    """
    # 딕셔너리를 DataFrame으로 변환
    data = []
    for key, value in result.items():
        data.append({
            'file_id': key,
            'prev_frame_start': value['prev_frame_start'],
            'prev_frame_end': value['prev_frame_end'],
            'current_frame_start': value['current_frame_start'],
            'current_frame_end': value['current_frame_end'],
            'activity': value['activity']
        })

    df = pd.DataFrame(data)

    # Markdown 형식 출력
    print(df.to_markdown())

# 예시 실행
mid_path = '/content/drive/MyDrive/sesac_final_project_dataset/annotations/activities_3s/kinect_color/midlevel.chunks_90.csv'
result = annotation_id_sensor(mid_path)

# 결과를 Markdown 형식으로 출력
# dict_to_markdown(result)

"""|    | file_id                                    |   prev_frame_start |   prev_frame_end |   current_frame_start |   current_frame_end | activity                   |
|---:|:-------------------------------------------|-------------------:|-----------------:|----------------------:|--------------------:|:---------------------------|
|  0 | vp1/run1b_2018-05-29-14-02-47.kinect_color |              17458 |            17467 |                 17522 |               17568 | sitting_still              |
|  1 | vp1/run2_2018-05-29-14-33-44.kinect_color  |              15557 |            15589 |                 15739 |               15784 | sitting_still              |
|  2 | vp2/run1_2018-05-03-14-08-31.kinect_color  |              14766 |            14774 |                 14791 |               14802 | using_multimedia_display   |
|  3 | vp2/run2_2018-05-24-17-22-26.kinect_color  |              19971 |            19976 |                 20060 |               20065 | pressing_automation_button |
|  4 | vp3/run1b_2018-05-08-08-46-01.kinect_color |              19934 |            19949 |                 19961 |               20006 | using_multimedia_display   |
|  5 | vp3/run2_2018-05-29-16-03-37.kinect_color  |              15754 |            15772 |                 15780 |               15785 | using_multimedia_display   |
|  6 | vp4/run1_2018-05-22-13-28-51.kinect_color  |              31294 |            31326 |                 31326 |               31373 | fetching_an_object         |
|  7 | vp4/run2_2018-05-22-14-25-04.kinect_color  |              22377 |            22382 |                 22725 |               22734 | using_multimedia_display   |
|  8 | vp5/run1_2018-05-22-15-10-41.kinect_color  |              25401 |            25433 |                 25501 |               25546 | sitting_still              |
|  9 | vp5/run2b_2018-05-22-15-50-07.kinect_color |              18770 |            18814 |                 18814 |               18860 | placing_an_object          |
| 10 | vp6/run1_2018-05-23-10-21-45.kinect_color  |              25670 |            25680 |                 25726 |               25736 | using_multimedia_display   |
| 11 | vp6/run2_2018-05-23-11-05-00.kinect_color  |              11478 |            11515 |                 11587 |               11633 | sitting_still              |
| 12 | vp7/run1_2018-05-23-13-16-52.kinect_color  |              15375 |            15394 |                 15582 |               15599 | using_multimedia_display   |
| 13 | vp7/run2b_2018-05-23-13-54-07.kinect_color |              11813 |            11843 |                 11843 |               11874 | fetching_an_object         |
| 14 | vp8/run1d_2018-05-23-14-54-38.kinect_color |              14088 |            14095 |                 14135 |               14145 | using_multimedia_display   |
| 15 | vp8/run2_2018-05-23-15-30-27.kinect_color  |              18971 |            19008 |                 19067 |               19109 | sitting_still              |
| 16 | vp9/run1b_2018-05-23-16-19-17.kinect_color |               9223 |             9245 |                  9245 |                9277 | taking_off_sunglasses      |
| 17 | vp10/run1_2018-05-24-13-14-41.kinect_color |              13967 |            13971 |                 14338 |               14344 | pressing_automation_button |
| 18 | vp10/run2_2018-05-24-14-08-46.kinect_color |              20600 |            20619 |                 20619 |               20653 | fetching_an_object         |
| 19 | vp11/run1_2018-05-24-13-44-01.kinect_color |              15320 |            15327 |                 15433 |               15443 | using_multimedia_display   |
| 20 | vp11/run2_2018-05-24-14-35-56.kinect_color |              11526 |            11547 |                 11568 |               11609 | placing_an_object          |
| 21 | vp12/run1_2018-05-24-15-44-28.kinect_color |              19400 |            19412 |                 19563 |               19607 | pressing_automation_button |
| 22 | vp12/run2_2018-05-24-16-21-35.kinect_color |              25154 |            25177 |                 25189 |               25201 | pressing_automation_button |
| 23 | vp13/run1_2018-05-29-15-21-10.kinect_color |              22497 |            22502 |                 22513 |               22518 | pressing_automation_button |
| 24 | vp13/run2_2018-05-30-11-34-54.kinect_color |              19864 |            19873 |                 19903 |               19908 | pressing_automation_button |
| 25 | vp14/run1_2018-05-30-10-11-09.kinect_color |              23828 |            23868 |                 24232 |               24235 | pressing_automation_button |
| 26 | vp14/run2_2018-05-30-10-42-33.kinect_color |              16918 |            16921 |                 17113 |               17158 | using_multimedia_display   |
| 27 | vp15/run1_2018-05-30-13-05-35.kinect_color |              18189 |            18199 |                 18306 |               18351 | sitting_still              |
| 28 | vp15/run2_2018-05-30-13-34-33.kinect_color |              18814 |            18860 |                 18953 |               18999 | sitting_still              |

### 상관관계 분석
"""



mid_path = '/content/drive/MyDrive/sesac_final_project_dataset/annotations/activities_3s/kinect_color/midlevel.chunks_90.csv'
df = pd.read_csv(mid_path)

# 문자형 데이터를 Label Encoding으로 변환
for col in ['file_id', 'activity']:
    df[col] = df[col].astype('category').cat.codes

# 숫자형 데이터만 추출
numeric_df = df[['participant_id', 'annotation_id', 'frame_start', 'frame_end',
                 'chunk_id', 'activity']]

# 상관관계 계산
correlation_matrix = numeric_df.corr()

# 상관관계 히트맵 시각화
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap with All Relevant Columns")
plt.show()

"""# object

### total_object 파일 head
"""

object_path = '/content/drive/MyDrive/sesac_final_project_dataset/annotations/activities_3s/kinect_color/objectlevel.chunks_90.csv'
df_object = pd.read_csv(object_path) # df = dataframe
print(df_object.head())

"""### total_object 동영상 목록"""

object_file_ids = df_object['file_id'].unique()
# print('file_ids : \n', mid_file_ids)
df = DataFrame(object_file_ids, columns = ['total_object_file_ids'])
# print(df.to_markdown())

"""|    | total_object_file_ids                      |
|---:|:-------------------------------------------|
|  0 | vp1/run1b_2018-05-29-14-02-47.kinect_color |
|  1 | vp1/run2_2018-05-29-14-33-44.kinect_color  |
|  2 | vp2/run1_2018-05-03-14-08-31.kinect_color  |
|  3 | vp2/run2_2018-05-24-17-22-26.kinect_color  |
|  4 | vp3/run1b_2018-05-08-08-46-01.kinect_color |
|  5 | vp3/run2_2018-05-29-16-03-37.kinect_color  |
|  6 | vp4/run1_2018-05-22-13-28-51.kinect_color  |
|  7 | vp4/run2_2018-05-22-14-25-04.kinect_color  |
|  8 | vp5/run1_2018-05-22-15-10-41.kinect_color  |
|  9 | vp5/run2b_2018-05-22-15-50-07.kinect_color |
| 10 | vp6/run1_2018-05-23-10-21-45.kinect_color  |
| 11 | vp6/run2_2018-05-23-11-05-00.kinect_color  |
| 12 | vp7/run1_2018-05-23-13-16-52.kinect_color  |
| 13 | vp7/run2b_2018-05-23-13-54-07.kinect_color |
| 14 | vp8/run1d_2018-05-23-14-54-38.kinect_color |
| 15 | vp8/run2_2018-05-23-15-30-27.kinect_color  |
| 16 | vp9/run1b_2018-05-23-16-19-17.kinect_color |
| 17 | vp10/run1_2018-05-24-13-14-41.kinect_color |
| 18 | vp10/run2_2018-05-24-14-08-46.kinect_color |
| 19 | vp11/run1_2018-05-24-13-44-01.kinect_color |
| 20 | vp11/run2_2018-05-24-14-35-56.kinect_color |
| 21 | vp12/run1_2018-05-24-15-44-28.kinect_color |
| 22 | vp12/run2_2018-05-24-16-21-35.kinect_color |
| 23 | vp13/run1_2018-05-29-15-21-10.kinect_color |
| 24 | vp13/run2_2018-05-30-11-34-54.kinect_color |
| 25 | vp14/run1_2018-05-30-10-11-09.kinect_color |
| 26 | vp14/run2_2018-05-30-10-42-33.kinect_color |
| 27 | vp15/run1_2018-05-30-13-05-35.kinect_color |
| 28 | vp15/run2_2018-05-30-13-34-33.kinect_color |

### total_object activity에 대한 count
"""

df = pd.read_csv(object_path)
activity_counts = df.groupby(['activity']).size().reset_index(name = 'count')

# print(activity_counts.to_markdown())

"""|    | activity          |   count |
|---:|:------------------|--------:|
|  0 | closing           |      82 |
|  1 | interacting       |    5691 |
|  2 | opening           |      89 |
|  3 | placing_moving_to |     748 |
|  4 | reaching_for      |    1576 |
|  5 | retracting_from   |    1783 |

### activity에 대한 count 막대그래프
"""

plot_activity_counts(object_path)

"""### total_object annotation_id 이상치"""

object_path = '/content/drive/MyDrive/sesac_final_project_dataset/annotations/activities_3s/kinect_color/objectlevel.chunks_90.csv'
result = annotation_id_sensor(object_path)

# dict_to_markdown(result)

"""|    | file_id                                    |   prev_frame_start |   prev_frame_end |   current_frame_start |   current_frame_end | activity          |
|---:|:-------------------------------------------|-------------------:|-----------------:|----------------------:|--------------------:|:------------------|
|  0 | vp1/run1b_2018-05-29-14-02-47.kinect_color |              17054 |            17088 |                 17150 |               17175 | reaching_for      |
|  1 | vp1/run2_2018-05-29-14-33-44.kinect_color  |              20649 |            20691 |                 20691 |               20716 | interacting       |
|  2 | vp2/run1_2018-05-03-14-08-31.kinect_color  |               9006 |             9030 |                  9030 |                9075 | interacting       |
|  3 | vp2/run2_2018-05-24-17-22-26.kinect_color  |              13874 |            13909 |                 13911 |               13942 | placing_moving_to |
|  4 | vp3/run1b_2018-05-08-08-46-01.kinect_color |              19166 |            19205 |                 19205 |               19215 | interacting       |
|  5 | vp3/run2_2018-05-29-16-03-37.kinect_color  |               6763 |             6781 |                  6781 |                6798 | interacting       |
|  6 | vp4/run1_2018-05-22-13-28-51.kinect_color  |              32838 |            32868 |                 32917 |               32938 | interacting       |
|  7 | vp4/run2_2018-05-22-14-25-04.kinect_color  |              24757 |            24769 |                 24769 |               24814 | interacting       |
|  8 | vp5/run1_2018-05-22-15-10-41.kinect_color  |              22033 |            22038 |                 22038 |               22074 | interacting       |
|  9 | vp5/run2b_2018-05-22-15-50-07.kinect_color |              18770 |            18814 |                 18814 |               18860 | placing_moving_to |
| 10 | vp6/run1_2018-05-23-10-21-45.kinect_color  |              26864 |            26872 |                 26872 |               26887 | retracting_from   |
| 11 | vp6/run2_2018-05-23-11-05-00.kinect_color  |              16897 |            16931 |                 16931 |               16976 | interacting       |
| 12 | vp7/run1_2018-05-23-13-16-52.kinect_color  |              17368 |            17371 |                 17371 |               17416 | interacting       |
| 13 | vp7/run2b_2018-05-23-13-54-07.kinect_color |              12144 |            12163 |                 12163 |               12177 | interacting       |
| 14 | vp8/run1d_2018-05-23-14-54-38.kinect_color |              22048 |            22063 |                 22063 |               22088 | reaching_for      |
| 15 | vp8/run2_2018-05-23-15-30-27.kinect_color  |              17982 |            18015 |                 18015 |               18060 | interacting       |
| 16 | vp9/run1b_2018-05-23-16-19-17.kinect_color |              12852 |            12892 |                 12892 |               12937 | interacting       |
| 17 | vp10/run1_2018-05-24-13-14-41.kinect_color |              13286 |            13296 |                 13298 |               13315 | reaching_for      |
| 18 | vp10/run2_2018-05-24-14-08-46.kinect_color |              19154 |            19164 |                 19164 |               19171 | interacting       |
| 19 | vp11/run1_2018-05-24-13-44-01.kinect_color |              18063 |            18105 |                 18105 |               18140 | interacting       |
| 20 | vp11/run2_2018-05-24-14-35-56.kinect_color |              12103 |            12145 |                 12145 |               12186 | interacting       |
| 21 | vp12/run1_2018-05-24-15-44-28.kinect_color |              19208 |            19229 |                 19229 |               19252 | retracting_from   |
| 22 | vp12/run2_2018-05-24-16-21-35.kinect_color |              16067 |            16094 |                 16094 |               16130 | placing_moving_to |
| 23 | vp13/run1_2018-05-29-15-21-10.kinect_color |              22817 |            22822 |                 22851 |               22876 | interacting       |
| 24 | vp13/run2_2018-05-30-11-34-54.kinect_color |              19864 |            19873 |                 19903 |               19908 | interacting       |
| 25 | vp14/run2_2018-05-30-10-42-33.kinect_color |               5972 |             5975 |                  5975 |                6020 | placing_moving_to |
| 26 | vp15/run1_2018-05-30-13-05-35.kinect_color |              17763 |            17766 |                 17766 |               17811 | interacting       |
| 27 | vp15/run2_2018-05-30-13-34-33.kinect_color |              12398 |            12408 |                 12408 |               12416 | reaching_for      |

### 상관관계
"""
object_path = '/content/drive/MyDrive/sesac_final_project_dataset/annotations/activities_3s/kinect_color/objectlevel.chunks_90.csv'
df = pd.read_csv(object_path)

# 문자형 데이터 -> Label Encoding
for col in ['file_id', 'activity', 'object', 'location']:
    df[col] = df[col].astype('category').cat.codes

# 숫자형 데이터만 추출 (모든 칼럼 포함)
numeric_df = df[['participant_id', 'file_id', 'annotation_id', 'frame_start',
                 'frame_end', 'chunk_id', 'activity', 'object', 'location']]

# 상관관계 계산
correlation_matrix = numeric_df.corr()

# 상관관계 히트맵 시각화
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap with All Relevant Columns")
plt.show()

"""# task

### total_task 파일 head
"""

task_path = r'C:\Final_project\data\activities_3s\kinect_color/tasklevel.chunks_90.csv'
df_task = pd.read_csv(task_path) # df = dataframe
print(df_task.head())

"""### total_task 동영상 목록"""

task_file_ids = df_task['file_id'].unique()
df = DataFrame(task_file_ids, columns = ['total_task_file_ids'])
# print(df.to_markdown())

"""|    | total_task_file_ids                        |
|---:|:-------------------------------------------|
|  0 | vp1/run1b_2018-05-29-14-02-47.kinect_color |
|  1 | vp1/run2_2018-05-29-14-33-44.kinect_color  |
|  2 | vp2/run1_2018-05-03-14-08-31.kinect_color  |
|  3 | vp2/run2_2018-05-24-17-22-26.kinect_color  |
|  4 | vp3/run1b_2018-05-08-08-46-01.kinect_color |
|  5 | vp3/run2_2018-05-29-16-03-37.kinect_color  |
|  6 | vp4/run1_2018-05-22-13-28-51.kinect_color  |
|  7 | vp4/run2_2018-05-22-14-25-04.kinect_color  |
|  8 | vp5/run1_2018-05-22-15-10-41.kinect_color  |
|  9 | vp5/run2b_2018-05-22-15-50-07.kinect_color |
| 10 | vp6/run1_2018-05-23-10-21-45.kinect_color  |
| 11 | vp6/run2_2018-05-23-11-05-00.kinect_color  |
| 12 | vp7/run1_2018-05-23-13-16-52.kinect_color  |
| 13 | vp7/run2b_2018-05-23-13-54-07.kinect_color |
| 14 | vp8/run1d_2018-05-23-14-54-38.kinect_color |
| 15 | vp8/run2_2018-05-23-15-30-27.kinect_color  |
| 16 | vp9/run1b_2018-05-23-16-19-17.kinect_color |
| 17 | vp10/run1_2018-05-24-13-14-41.kinect_color |
| 18 | vp10/run2_2018-05-24-14-08-46.kinect_color |
| 19 | vp11/run1_2018-05-24-13-44-01.kinect_color |
| 20 | vp11/run2_2018-05-24-14-35-56.kinect_color |
| 21 | vp12/run1_2018-05-24-15-44-28.kinect_color |
| 22 | vp12/run2_2018-05-24-16-21-35.kinect_color |
| 23 | vp13/run1_2018-05-29-15-21-10.kinect_color |
| 24 | vp13/run2_2018-05-30-11-34-54.kinect_color |
| 25 | vp14/run1_2018-05-30-10-11-09.kinect_color |
| 26 | vp14/run2_2018-05-30-10-42-33.kinect_color |
| 27 | vp15/run1_2018-05-30-13-05-35.kinect_color |
| 28 | vp15/run2_2018-05-30-13-34-33.kinect_color |

### total_task activity에 대한 count
"""

df = pd.read_csv(task_path)
activity_counts = df.groupby(['activity']).size().reset_index(name = 'count')

# print(activity_counts.to_markdown())

"""|    | activity             |   count |
|---:|:---------------------|--------:|
|  0 | eat_drink            |    1277 |
|  1 | fasten_seat_belt     |     362 |
|  2 | final_task           |     352 |
|  3 | hand_over            |     141 |
|  4 | put_on_jacket        |     412 |
|  5 | put_on_sunglasses    |     193 |
|  6 | read_write_magazine  |    1181 |
|  7 | read_write_newspaper |    1023 |
|  8 | take_off_jacket      |     261 |
|  9 | take_off_sunglasses  |     171 |
| 10 | watch_video          |    1892 |
| 11 | work                 |    1214 |

### activity에 대한 count 막대그래프
"""

plot_activity_counts(task_path)

"""### total_task annotation_id 이상치"""

task_path = 'C:\Final_project\data\activities_3s\kinect_color/tasklevel.chunks_90.csv'
result = annotation_id_sensor(task_path)

# dict_to_markdown(result)

"""|    | file_id                                    |   prev_frame_start |   prev_frame_end |   current_frame_start |   current_frame_end | activity   |
|---:|:-------------------------------------------|-------------------:|-----------------:|----------------------:|--------------------:|:-----------|
|  0 | vp6/run1_2018-05-23-10-21-45.kinect_color  |              20796 |            20836 |                 21098 |               21144 | eat_drink  |
|  1 | vp12/run2_2018-05-24-16-21-35.kinect_color |              18212 |            18233 |                 19265 |               19311 | eat_drink  |

### 상관관계 분석
"""
df = pd.read_csv(object_path)

# 문자형 데이터 -> Label Encoding
for col in ['file_id', 'activity']:
    df[col] = df[col].astype('category').cat.codes

# 숫자형 데이터만 추출 (모든 칼럼 포함)
numeric_df = df[['participant_id', 'file_id', 'annotation_id', 'frame_start',
                 'frame_end', 'chunk_id', 'activity']]

# 상관관계 계산
correlation_matrix = numeric_df.corr()

# 상관관계 히트맵 시각화
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap with All Relevant Columns")
plt.show()


