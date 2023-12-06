# Seamless Translation

Seamless-m4t-v2-large is a multimodal speech detection and translation model.

More information is available on the model [card](https://huggingface.co/facebook/seamless-m4t-v2-large)

Google Colab available [here](https://colab.research.google.com/drive/1ndSYhHxPkMl58EpkZ5pWrfsTxYgMhwWO?usp=sharing)

![header](assets/header.png)

![Python](https://img.shields.io/badge/Python-3.8-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFEF00?style=flat&logo=HuggingFace&logoColor=black)


## Installation

To install Seamless Translation, follow these steps:

```bash
git clone 
cd seamless-translation
pip install -r requirements.txt
```

## Usage

After installation, you can easily run the application using Streamlit. Use the following command to start the application:

```bash
streamlit run app.py
```

## Features

Seamless Translation offers a comprehensive range of features:

+ Multilingual Support: It supports an extensive list of languages and dialects, with capabilities for both speech and text translation.
+ Speech and Text Input: The model can process both spoken words (Sp) and textual data (Tx), offering flexibility in usage.
+ Diverse Script Handling: It accommodates a wide array of scripts, including Latin, Cyrillic, Arabic, and more, ensuring accurate translation across different writing systems.
+ Seamless Communication: Designed for both source and target language translation, the model provides a smooth and efficient translation process.

## Testing

Test the model and cache the download to make the streamlit script startup faster:

```
python test.py
```

### Supported Languages 

| code | language               | script     | Source | Target |
| ---- | ---------------------- | ---------- | ------ | ------ |
| afr  | Afrikaans              | Latn       | Sp, Tx | Tx     |
| amh  | Amharic                | Ethi       | Sp, Tx | Tx     |
| arb  | Modern Standard Arabic | Arab       | Sp, Tx | Sp, Tx |
| ary  | Moroccan Arabic        | Arab       | Sp, Tx | Tx     |
| arz  | Egyptian Arabic        | Arab       | Sp, Tx | Tx     |
| asm  | Assamese               | Beng       | Sp, Tx | Tx     |
| ast  | Asturian               | Latn       | Sp     | \--    |
| azj  | North Azerbaijani      | Latn       | Sp, Tx | Tx     |
| bel  | Belarusian             | Cyrl       | Sp, Tx | Tx     |
| ben  | Bengali                | Beng       | Sp, Tx | Sp, Tx |
| bos  | Bosnian                | Latn       | Sp, Tx | Tx     |
| bul  | Bulgarian              | Cyrl       | Sp, Tx | Tx     |
| cat  | Catalan                | Latn       | Sp, Tx | Sp, Tx |
| ceb  | Cebuano                | Latn       | Sp, Tx | Tx     |
| ces  | Czech                  | Latn       | Sp, Tx | Sp, Tx |
| ckb  | Central Kurdish        | Arab       | Sp, Tx | Tx     |
| cmn  | Mandarin Chinese       | Hans       | Sp, Tx | Sp, Tx |
| cmn_Hant  | Mandarin Chinese  | Hant       | Sp, Tx | Sp, Tx |
| cym  | Welsh                  | Latn       | Sp, Tx | Sp, Tx |
| dan  | Danish                 | Latn       | Sp, Tx | Sp, Tx |
| deu  | German                 | Latn       | Sp, Tx | Sp, Tx |
| ell  | Greek                  | Grek       | Sp, Tx | Tx     |
| eng  | English                | Latn       | Sp, Tx | Sp, Tx |
| est  | Estonian               | Latn       | Sp, Tx | Sp, Tx |
| eus  | Basque                 | Latn       | Sp, Tx | Tx     |
| fin  | Finnish                | Latn       | Sp, Tx | Sp, Tx |
| fra  | French                 | Latn       | Sp, Tx | Sp, Tx |
| fuv  | Nigerian Fulfulde      | Latn       | Sp, Tx | Tx     |
| gaz  | West Central Oromo     | Latn       | Sp, Tx | Tx     |
| gle  | Irish                  | Latn       | Sp, Tx | Tx     |
| glg  | Galician               | Latn       | Sp, Tx | Tx     |
| guj  | Gujarati               | Gujr       | Sp, Tx | Tx     |
| heb  | Hebrew                 | Hebr       | Sp, Tx | Tx     |
| hin  | Hindi                  | Deva       | Sp, Tx | Sp, Tx |
| hrv  | Croatian               | Latn       | Sp, Tx | Tx     |
| hun  | Hungarian              | Latn       | Sp, Tx | Tx     |
| hye  | Armenian               | Armn       | Sp, Tx | Tx     |
| ibo  | Igbo                   | Latn       | Sp, Tx | Tx     |
| ind  | Indonesian             | Latn       | Sp, Tx | Sp, Tx |
| isl  | Icelandic              | Latn       | Sp, Tx | Tx     |
| ita  | Italian                | Latn       | Sp, Tx | Sp, Tx |
| jav  | Javanese               | Latn       | Sp, Tx | Tx     |
| jpn  | Japanese               | Jpan       | Sp, Tx | Sp, Tx |
| kam  | Kamba                  | Latn       | Sp     | \--    |
| kan  | Kannada                | Knda       | Sp, Tx | Tx     |
| kat  | Georgian               | Geor       | Sp, Tx | Tx     |
| kaz  | Kazakh                 | Cyrl       | Sp, Tx | Tx     |
| kea  | Kabuverdianu           | Latn       | Sp     | \--    |
| khk  | Halh Mongolian         | Cyrl       | Sp, Tx | Tx     |
| khm  | Khmer                  | Khmr       | Sp, Tx | Tx     |
| kir  | Kyrgyz                 | Cyrl       | Sp, Tx | Tx     |
| kor  | Korean                 | Kore       | Sp, Tx | Sp, Tx |
| lao  | Lao                    | Laoo       | Sp, Tx | Tx     |
| lit  | Lithuanian             | Latn       | Sp, Tx | Tx     |
| ltz  | Luxembourgish          | Latn       | Sp     | \--    |
| lug  | Ganda                  | Latn       | Sp, Tx | Tx     |
| luo  | Luo                    | Latn       | Sp, Tx | Tx     |
| lvs  | Standard Latvian       | Latn       | Sp, Tx | Tx     |
| mai  | Maithili               | Deva       | Sp, Tx | Tx     |
| mal  | Malayalam              | Mlym       | Sp, Tx | Tx     |
| mar  | Marathi                | Deva       | Sp, Tx | Tx     |
| mkd  | Macedonian             | Cyrl       | Sp, Tx | Tx     |
| mlt  | Maltese                | Latn       | Sp, Tx | Sp, Tx |
| mni  | Meitei                 | Beng       | Sp, Tx | Tx     |
| mya  | Burmese                | Mymr       | Sp, Tx | Tx     |
| nld  | Dutch                  | Latn       | Sp, Tx | Sp, Tx |
| nno  | Norwegian Nynorsk      | Latn       | Sp, Tx | Tx     |
| nob  | Norwegian Bokmål       | Latn       | Sp, Tx | Tx     |
| npi  | Nepali                 | Deva       | Sp, Tx | Tx     |
| nya  | Nyanja                 | Latn       | Sp, Tx | Tx     |
| oci  | Occitan                | Latn       | Sp     | \--    |
| ory  | Odia                   | Orya       | Sp, Tx | Tx     |
| pan  | Punjabi                | Guru       | Sp, Tx | Tx     |
| pbt  | Southern Pashto        | Arab       | Sp, Tx | Tx     |
| pes  | Western Persian        | Arab       | Sp, Tx | Sp, Tx |
| pol  | Polish                 | Latn       | Sp, Tx | Sp, Tx |
| por  | Portuguese             | Latn       | Sp, Tx | Sp, Tx |
| ron  | Romanian               | Latn       | Sp, Tx | Sp, Tx |
| rus  | Russian                | Cyrl       | Sp, Tx | Sp, Tx |
| slk  | Slovak                 | Latn       | Sp, Tx | Sp, Tx |
| slv  | Slovenian              | Latn       | Sp, Tx | Tx     |
| sna  | Shona                  | Latn       | Sp, Tx | Tx     |
| snd  | Sindhi                 | Arab       | Sp, Tx | Tx     |
| som  | Somali                 | Latn       | Sp, Tx | Tx     |
| spa  | Spanish                | Latn       | Sp, Tx | Sp, Tx |
| srp  | Serbian                | Cyrl       | Sp, Tx | Tx     |
| swe  | Swedish                | Latn       | Sp, Tx | Sp, Tx |
| swh  | Swahili                | Latn       | Sp, Tx | Sp, Tx |
| tam  | Tamil                  | Taml       | Sp, Tx | Tx     |
| tel  | Telugu                 | Telu       | Sp, Tx | Sp, Tx |
| tgk  | Tajik                  | Cyrl       | Sp, Tx | Tx     |
| tgl  | Tagalog                | Latn       | Sp, Tx | Sp, Tx |
| tha  | Thai                   | Thai       | Sp, Tx | Sp, Tx |
| tur  | Turkish                | Latn       | Sp, Tx | Sp, Tx |
| ukr  | Ukrainian              | Cyrl       | Sp, Tx | Sp, Tx |
| urd  | Urdu                   | Arab       | Sp, Tx | Sp, Tx |
| uzn  | Northern Uzbek         | Latn       | Sp, Tx | Sp, Tx |
| vie  | Vietnamese             | Latn       | Sp, Tx | Sp, Tx |
| xho  | Xhosa                  | Latn       | Sp     | \--    |
| yor  | Yoruba                 | Latn       | Sp, Tx | Tx     |
| yue  | Cantonese              | Hant       | Sp, Tx | Tx     |
| zlm  | Colloquial Malay       | Latn       | Sp     | \--    |
| zsm  | Standard Malay         | Latn       | Tx     | Tx     |
| zul  | Zulu                   | Latn       | Sp, Tx | Tx     |


### Citations


```bibtex
@inproceedings{seamless2023,
   title="Seamless: Multilingual Expressive and Streaming Speech Translation",
   author="{Seamless Communication}, Lo{\"i}c Barrault, Yu-An Chung, Mariano Coria Meglioli, David Dale, Ning Dong, Mark Duppenthaler, Paul-Ambroise Duquenne, Brian Ellis, Hady Elsahar, Justin Haaheim, John Hoffman, Min-Jae Hwang, Hirofumi Inaguma, Christopher Klaiber, Ilia Kulikov, Pengwei Li, Daniel Licht, Jean Maillard, Ruslan Mavlyutov, Alice Rakotoarison, Kaushik Ram Sadagopan, Abinesh Ramakrishnan, Tuan Tran, Guillaume Wenzek, Yilin Yang, Ethan Ye, Ivan Evtimov, Pierre Fernandez, Cynthia Gao, Prangthip Hansanti, Elahe Kalbassi, Amanda Kallet, Artyom Kozhevnikov, Gabriel Mejia, Robin San Roman, Christophe Touret, Corinne Wong, Carleigh Wood, Bokai Yu, Pierre Andrews, Can Balioglu, Peng-Jen Chen, Marta R. Costa-juss{\`a}, Maha Elbayad, Hongyu Gong, Francisco Guzm{\'a}n, Kevin Heffernan, Somya Jain, Justine Kao, Ann Lee, Xutai Ma, Alex Mourachko, Benjamin Peloquin, Juan Pino, Sravya Popuri, Christophe Ropers, Safiyyah Saleem, Holger Schwenk, Anna Sun, Paden Tomasello, Changhan Wang, Jeff Wang, Skyler Wang, Mary Williamson",
  journal={ArXiv},
  year={2023}
}

```