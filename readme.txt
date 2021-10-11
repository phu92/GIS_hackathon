@본 문서는 해당 파일의 설치와 기능 설명으로 구성되어있습니다.@

*anaconda3와 VSC(visual studio code) 및 파이썬 설치 필수

해당 깃을 클론하거나 폴더에 저장하신 후 git clone https://github.com/phu92/GIS_hackathon

1. VSC에서 F1키 누른 후 Select Interpreter 검색
	목록에서 아나콘다 환경의 파이썬 선택
	ex) python 3.8.8 64-bit 
		~\anaconda3\envs\likelion\python.exe 

2 . VSC에서 F1키 누른 후 Terminal Select Defualt Profile 검색
	Command Prompt 선택
	터미널(T)에서 새 터미널 열기
	터미널에 conda activate base가 자동으로 입력되는 것을 확인하기

3. 터미널에 명령어 입력
	(base) >> conda create -n likelion python=3.8.8                  #새로운 가상환경생성
	(likelion) >> conda activate likelion                                         #가상환경 사용자 변경하기
	(likelion) >> pip install -r requirements.txt 		# 해당 명령어를 터미널에 입력하여 모듈을 설치해주세요.
	(likelion) >> streamlit run solar.py		              #실행파일 streamlit으로 실행하기
# 스트림릿 첫 실행시 나오는 email 입력은 Enter로 스킵하시면 됩니다.

=================================================================================

해당 파일의 기능

1. 좌측 사이드바의 신재생에너지 테스트
	5가지 항목을 모두 입력하고 결과 출력을 해보신 후
	사이드바 하단의 테스트 결과 이미지를 확인해보세요
	지열, 태양광, 풍력, 수력, 수소 5가지로 구성되어있습니다.

2. 태양광 데이터 출력 및 저장 기능
	지역을 선택하여 발전량, 일사량, 온도 등을 확인 및 저장할 수 있습니다.
	해당 데이터는 날씨마루 https://bd.kma.go.kr/kma2020/fs/energySelect1.do?pageNum=5&menuCd=F050701000 에서 가져왔으며
	처음 데이터로딩 시 30초의 시간이 소요 됩니다.
	표 밑에 생성되는[표 데이터를 저장할 수 있습니다.] 버튼을 눌러 CSV 파일을 저장할 수 있습니다.

3. 하늘 상태 분류 기능
	스트림릿 자체의 저장공간 문제로 인하여 해당 파일에서는 실행되지 않습니다.
	최하단의 모델예시를 통하여 작동예시와 사용된 코드를 확인할 수 있으며
	또는 image_classifi.py 파일에서 이미지 경로를 입력 후 직접 확인해 볼 수 있습니다.

	해당 파일은 '맑은 날', '흐린 날', '일몰 혹은 일출'의 3가지 결과가 출력되며
	향후 IOT센서(카메라 센서 및 조도 센서)와 이미지 분류를 결합하여 데이터를 측정,
	하늘 사진만 업로드해도 일사량과 태양광 발전 적합도를 출력하는 것을 목표로 하고 있습니다. 

4. 태양광 탄소 배출량 계산
	한국 전력의 전기 생산 1KWh당 탄소 발생량 (0.424kg)
	2012년 산림청 국립산림과학원의 정책브리핑 자료 ('우리나라 소나무 30년생 1ha의 숲은 매년 10.8톤의 CO2를 흡수함으로써,')
	그리고 IPCC의(기후 변화에 관한 정부간 협의체) 발전원별 생애주기 탄소배출량 자료를 환산하여 계산하였습니다.
	
=================================================================================
정부 브리핑 자료 - 제5차 신재생에너지 기본계획 참조
신재생에너지원별 발전 비중 목표~
https://www.knrec.or.kr/download/file_download.aspx?key=1682&gubun=notice&div=FILE_NM2

저작권이 없는 이미지 및 폰트를 사용하였습니다.
폰트 : 카페24 써라운드
이미지 : 
	메인 : https://pixabay.com/ko/photos/%ED%83%9C%EC%96%91%EA%B4%91-%EA%B3%B5%EC%9B%90-%ED%92%8D%EB%A0%A5-%EB%B0%9C%EC%A0%84-%EB%8B%A8%EC%A7%80-1288842/
	지열 : https://pixabay.com/ko/photos/%eb%a7%88%ec%9a%b4%ed%8a%b8-%ed%9b%84-%ec%a7%80-%ed%99%94%ec%82%b0-%ec%9d%bc%eb%b3%b8-264267/
	태양광 : https://www.publicdomainpictures.net/en/view-image.php?image=268930&picture=solar-energy-business
	풍력 : https://pixabay.com/illustrations/wind-energy-socket-environmental-4091082/
	수소 : https://commons.wikimedia.org/wiki/File:RH2cycle.png
	수력 : https://pixabay.com/es/photos/represa-r%C3%ADo-agua-paisaje-poder-929406/
