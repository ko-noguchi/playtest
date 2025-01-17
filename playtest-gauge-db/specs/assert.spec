# テーブルのアサートをする
tags: _setup

## カラムの値を指定して、文字列をアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、"id"を"'404e05a3-a34f-47d0-8997-968d90ba64ca'"で取得した一意の"memo"が文字列の"this is test"である

## カラムの値を指定して、整数をアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、"id"を"'404e05a3-a34f-47d0-8997-968d90ba64ca'"で取得した一意の"priority"が整数の"1"である

## カラムの値を指定して、小数をアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、"id"を"'404e05a3-a34f-47d0-8997-968d90ba64ca'"で取得した一意の"progress_rate"が小数の"0.1"である

## カラムの値を指定して、日付をアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、"id"を"'404e05a3-a34f-47d0-8997-968d90ba64ca'"で取得した一意の"registered_date"が"2021"年"10"月"1"日である

## カラムの値を指定して、日時をアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、"id"を"'404e05a3-a34f-47d0-8997-968d90ba64ca'"で取得した一意の"updated_date"が日時の"2021-11-15T01:12:33"である

## カラムの値を指定して、NULLをアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、"id"を"'304e05a3-a34f-47d0-8997-968d90ba64ca'"で取得した一意の"memo"がNULLである

## 存在しないことをアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルに、"id"が"'604e05a3-a34f-47d0-8997-968d90ba64ca'"なレコードが存在しない

## 条件文で取得したレコードの、文字列のフィールドをアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、条件" id = '404e05a3-a34f-47d0-8997-968d90ba64ca' "で取得した一意の"memo"が文字列の"this is test"である

## 条件文で取得したレコードの、整数のフィールドをアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、条件" id = '404e05a3-a34f-47d0-8997-968d90ba64ca' "で取得した一意の"priority"が整数の"1"である

## 条件文で取得したレコードの、小数のフィールドをアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、条件" id = '404e05a3-a34f-47d0-8997-968d90ba64ca' "で取得した一意の"progress_rate"が小数の"0.1"である

## 条件文で取得したレコードの、日付のフィールドをアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、条件" id = '404e05a3-a34f-47d0-8997-968d90ba64ca' "で取得した一意の"registered_date"が"2021"年"10"月"1"日である

## 条件文で取得したレコードの、日時のフィールドをアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、条件" id = '404e05a3-a34f-47d0-8997-968d90ba64ca' "で取得した一意の"updated_date"が日時の"2021-11-15T01:12:33"である

## 条件文で取得したレコードの、NULLのフィールドをアサートする
* DB"test_db"の"test"スキーマの"todos"テーブルの、条件" id = '304e05a3-a34f-47d0-8997-968d90ba64ca' "で取得した一意の"memo"がNULLである

## 条件文で取得したレコードが存在しない
* DB"test_db"の"test"スキーマの"todos"テーブルに、条件" id = '504e05a3-a34f-47d0-8997-968d90ba64ca' "なレコードが存在しない

record-changesタグが付与されたシナリオは、シナリオが始まったタイミングから、1つ目の変化数のアサートのタイミングまでのDBの変化を記録する
## 指定したテーブルで変更されたレコード数をアサートする
tags: record-changes
* [not-provide] test_dbのtodoテーブルのレコードをアップデートする
* DB"test_db"の"test"スキーマの"todos"テーブルで変更されたレコード数が"1"である

## 指定したテーブルで削除されたレコード数をアサートする
tags: record-changes
* [not-provide] test_dbのtodoテーブルのid"404e05a3-a34f-47d0-8997-968d90ba64ca"のレコードを削除する
* DB"test_db"の"test"スキーマの"todos"テーブルで削除されたレコード数が"1"である

## 指定したテーブルで作成されたレコード数をアサートする
tags: record-changes
* [not-provide] test_dbのtodoテーブルにレコードを挿入する
* DB"test_db"の"test"スキーマの"todos"テーブルで作成されたレコード数が"1"である

## Stepによる記録開始タイミングの制御
* start-record
* [not-provide] test_dbのtodoテーブルのレコードをアップデートする
* DB"test_db"の"test"スキーマの"todos"テーブルで変更されたレコード数が"1"である
