# Simba 介紹 #

這是一個支援自動產生 Django Project 以及加入部分修正的支援系統

### 怎麼安裝? ###

#### 需求 ： python3.7

1. 克隆到自己目錄下
2. cd simba
3. pipenv install  【安裝虛擬環境，如果沒有請先安裝pipenv】


### 怎麼使用？
------

```shell
python main.py createproject -h
```

```html
usage: main.py [-h] [-n NAME] [-p PATH] [-c]
	[--delproject DELPROJECT DELPROJECT]
    newproject

 Calamus & Glider's Django auto generate tool

 positional arguments:
	newproject            create Django project's base structure

	optional arguments:
  		-h, --help            show this help message and exit
  		-n NAME, --name NAME  Django project name
  		-p PATH, --path PATH  Django project path
  		-c, --channels        Add channels settings
  		--delproject DELPROJECT DELPROJECT
	delete Django project's base structure
```

------

#### 建立專案範例
```shell
python main.py newproject -n `project name` -c `channels` -p `project folder path`
```
