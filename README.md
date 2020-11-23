# 너.. 약간 포켓몬 닮은 것 같은데?
`2020 무박2일 khuthon TEAMBulgari`  
  
당신의 사진을 전달하면, 가장 닮은 포켓몬을 알려드립니다. 또한 해당 포켓몬과 몇 퍼센트의 일치율을 갖는지도 서비스로 알려드립니다.  

학습된 모델은 [`배포본: media/page/files/final_model.hdf`](https://github.com/TEAMbulgari/pokemon_deploy/tree/main/media/page/files)에서 확인하실 수 있으며, 모델의 학습 과정은 `포켓몬닮은꼴모델_학습과정.ipynb`에서 확인할 수 있습니다.  
  
[너.. 약간 포켓몬 닮은 것 같은데? 실행하기](https://pokemon-like-me.herokuapp.com/)  
[배포용 프로젝트 깃허브](https://github.com/TEAMbulgari/pokemon_deploy)

**팀원**
- 김수현: `포켓몬 닮은꼴 모델 개발` `모델 학습`
- 박승혜: `back-end` `front-end`
- 서민정: `back-end` `data-crawling` `deploy`
- 이동주: `data-crawling` `data-preprocessing`

## Stack
`keras` `tensorflow` `Django` `python` `heroku`

## 필요 모듈 설치
```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## 실행 방법
```
python manage.py runserver
```

## Github
김수현 https://github.com/iwillbeaprogramer  
박승혜 https://github.com/con11234  
서민정 https://github.com/seovalue  
이동주 https://github.com/djlee514 
