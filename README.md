WordCloud App
====
文章を読み込みして、どんな単語が多く含まれているのかを画像として生成します。

## Description
日本語のみ対応。  
Mecabを用いて単語を形態素解析したのち、形容詞・動詞・名詞を抽出します。  
抽出した単語の出現回数をカウントして、一番大きい物を強調して画像データとして出力します。

## Demo
![demo](https://github.com/NaotoWada/wordcloud/blob/master/wc.png)

## Requirement
* matplotlib==3.0.3
* mecab-python3==0.7
* pandas==0.24.2
* Pillow==6.0.0
* wordcloud==1.5.0

## Usage
クローンした[data/sample.csv](https://github.com/NaotoWada/wordcloud/blob/master/data/sample.csv)の`title`以降の行を編集して、以下コマンドを実行します。  

```
python3 application_execute.py
```

`application_execute.py`と同階層のディレクトリに`wc.png`ファイルが生成されています。

## Install
各自環境にcloneして実行してください。

## Author

[NaotoWada](https://github.com/NaotoWada)
