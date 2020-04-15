# conj
Simple Japanese conjugation generator

## Usage
A minimum interactive shell is provided. Basic syntax is `command romaji`.

## Available Commands:
+ `help`
+ `te`: テform of given verb
+ compound commands:
    + `ad` for adjective
    + `n` for noun
    + `v` for verb
    + `pr` for present
    + `pa` for past
    + `l` for long form
    + `s` for short form
    + `1` for affirmative
    + `0` for negative
    
Order does not matter, BUT these flags must be used without typo!
   
## Examples and tests
```
> nprl1 hagaki
はがきです
> nprl0 hagaki
はがきじゃないです
> nprs1 hagaki
はがきだ
> nprs0 hagaki
はがきじゃない
> npal1 hagaki
はがきでした
> npal0 hagaki
はがきじゃなかったです
> npas1 hagaki
はがきだった
> npas0 hagaki
はがきじゃなかった


> adprl1 kawaii
かわいいです
> adprl0 kawaii
かわいくないです
> adprs1 kawaii
かわいい
> adprs0 kawaii
かわいくない
> adpal1 kawaii
かわいかったです
> adpal0 kawaii
かわいくなかったです
> adpas1 kawaii
かわいかった
> adpas0 kawaii
かわいくなかった


> vprl1 nomu
みます
> vprl0 nomu
のみません
> vprs1 nomu
のむ
> vprs0 nomu
のまない
> vpal1 nomu
のみました
> vpal0 nomu
のみませんでした
> vpas1 nomu
のんだ
> vpas0 nomu
のまなかった
```


## Requirements
[romkan](https://pypi.org/project/romkan/) for Hiragana transcription 
