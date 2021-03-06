from django.core.management.base import BaseCommand
from checklists.models import CheckListQuestion


NAME = "check list"


class Command(BaseCommand):

    help = f"This commend creates {NAME}"

    def handle(self, *args, **options):
        questions = [
            {"question": "눈이 시고 눈물이난다", "element": "ELEMENT_WOOD"},
            {"question": "안구가 건조하다", "element": "ELEMENT_WOOD"},
            {"question": "편두통이 있다", "element": "ELEMENT_WOOD"},
            {"question": "피부가 건조하고 가려움증이 있다 ", "element": "ELEMENT_WOOD"},
            {"question": "목이 잘 쉬고 가래가 낀다 ", "element": "ELEMENT_WOOD"},
            {"question": "옆구리가 결리고 다리에 쥐가 잘난다 ", "element": "ELEMENT_WOOD"},
            {"question": "불면증, 수면장애 ", "element": "ELEMENT_WOOD"},
            {"question": "목감기가 잘 오고 편도선에 이상이 있다 ", "element": "ELEMENT_WOOD"},
            {"question": "구역질이 잘 나고 소화가 잘 안된다", "element": "ELEMENT_WOOD"},
            {"question": "밥맛이 없고 면,빵등 밀가루 음식을 찾는다", "element": "ELEMENT_WOOD"},
            {"question": "다리가 안으로 혹은 밖으로 휘어 있다", "element": "ELEMENT_WOOD"},
            {"question": "고관절이 안좋다 ", "element": "ELEMENT_WOOD"},
            {"question": "발이 잘 피곤하다 ", "element": "ELEMENT_WOOD"},
            {"question": "걸음이 빠르고 성격이 급하다", "element": "ELEMENT_WOOD"},
            {"question": "쉬지 못하고 계속 무언가를 한다", "element": "ELEMENT_WOOD"},
            {"question": "못마땅하고 거슬리는 것이 많다", "element": "ELEMENT_WOOD"},
            {"question": "가슴이 답답하고 한숨을 잘 쉰다", "element": "ELEMENT_WOOD"},
            {"question": "나도 모르게 욱하고 화가 난다 ", "element": "ELEMENT_WOOD"},
            {"question": "딸꾹질을 잘 한다", "element": "ELEMENT_FIRE"},
            {"question": "눈에 다래끼가 잘 나거나 충혈이 잘 된다", "element": "ELEMENT_FIRE"},
            {"question": "깜짝깜짝 놀란다", "element": "ELEMENT_FIRE"},
            {"question": "윗팔뚝이 굵거나 닭살이 있다 ", "element": "ELEMENT_FIRE"},
            {"question": "팔꿈치나 날갯죽지가 잘 아프다 ", "element": "ELEMENT_FIRE"},
            {"question": "얼굴이 붉은편이고 특히 볼이 잘 빨개진다 ", "element": "ELEMENT_FIRE"},
            {"question": "광대뼈 주변에 기미 주근깨가 있다 ", "element": "ELEMENT_FIRE"},
            {"question": "새끼 손가락에 이상이 있다 (짧거나 꼬부라짐) ",
             "element": "ELEMENT_FIRE"},
            {"question": "혓바늘이 잘 돋거나 혀가 갈라지는등 혀에 이상이 있다", "element": "ELEMENT_FIRE"},
            {"question": "가슴이 두근거린다 ", "element": "ELEMENT_FIRE"},
            {"question": "조금만 걸어도 숨이찬다 ", "element": "ELEMENT_FIRE"},
            {"question": "부탁을 하면 거절을 잘 못한다", "element": "ELEMENT_FIRE"},
            {"question": "먼저 말 걸어오기전에는 인사를 잘 안한다", "element": "ELEMENT_FIRE"},
            {"question": "웃고 싶지 않은데 웃음이 난다", "element": "ELEMENT_FIRE"},
            {"question": "말끝을 흐린다", "element": "ELEMENT_FIRE"},
            {"question": "말을 더듬는다", "element": "ELEMENT_FIRE"},
            {"question": "꿈을 많이 꾼다", "element": "ELEMENT_FIRE"},
            {"question": "화병이 있다", "element": "ELEMENT_FIRE"},
            {"question": "입맛이 까다롭지 않고 식사량이 많다 ", "element": "ELEMENT_EARTH"},
            {"question": "얼굴이 누르끼리하고 개기름이 낀다 ", "element": "ELEMENT_EARTH"},
            {"question": "무릎이 시큰거리고 앉았다 일어 날 때 빨리 펴지 못한다 ",
                "element": "ELEMENT_EARTH"},
            {"question": "물을 많이 마시고 특히 찬물을 좋아한다 ", "element": "ELEMENT_EARTH"},
            {"question": "눈꺼풀이 떨리거나 손이 떨린다 ", "element": "ELEMENT_EARTH"},
            {"question": "눈밑이 불룩하게 나와있다 ", "element": "ELEMENT_EARTH"},
            {"question": "입술이 잘 부르트고 입병이 잘난다 ", "element": "ELEMENT_EARTH"},
            {"question": "윗배가 나오고 전반적으로 군살이 많다 ", "element": "ELEMENT_EARTH"},
            {"question": "피부에 멍이 잘든다 ", "element": "ELEMENT_EARTH"},
            {"question": "누워있기 좋아 한다", "element": "ELEMENT_EARTH"},
            {"question": "달콤한 것을 좋아하지만 살이 찔까봐 마음껏 못 먹는다", "element": "ELEMENT_EARTH"},
            {"question": "생각이 많다", "element": "ELEMENT_EARTH"},
            {"question": "의심을 많이 한다", "element": "ELEMENT_EARTH"},
            {"question": "같은 얘기를 반복하거나 같은 노래를 계속 흥얼거린다", "element": "ELEMENT_EARTH"},
            {"question": "계획만 세우고 실천을 잘 못한다", "element": "ELEMENT_EARTH"},
            {"question": "약속 시간을 잘 못 지킨다", "element": "ELEMENT_EARTH"},
            {"question": "게을러지고 일을 미룬다", "element": "ELEMENT_EARTH"},
            {"question": "걱정이 많다", "element": "ELEMENT_EARTH"},
            {"question": "콧물, 재채기가 잘 난다", "element": "ELEMENT_METAL"},
            {"question": "피부가 탄력이 없고 늘어져 있다", "element": "ELEMENT_METAL"},
            {"question": "얼굴이 허옇고 창백하다", "element": "ELEMENT_METAL"},
            {"question": "치질, 치루가 있다", "element": "ELEMENT_METAL"},
            {"question": "숨이 차다", "element": "ELEMENT_METAL"},
            {"question": "코가 막히고 냄새를 잘 못 맡는다", "element": "ELEMENT_METAL"},
            {"question": "손목이 약하고 아귀힘이 없다", "element": "ELEMENT_METAL"},
            {"question": "엄지 손가락이 자주 아프다", "element": "ELEMENT_METAL"},
            {"question": "건조한 것을 싫어한다", "element": "ELEMENT_METAL"},
            {"question": "허리 아래가 빠지듯 아프다", "element": "ELEMENT_METAL"},
            {"question": "등이 굽고 아랫배를 내미는 자세로 걷는다", "element": "ELEMENT_METAL"},
            {"question": "설사를 잘하고 변이 묽다", "element": "ELEMENT_METAL"},
            {"question": "매운 것을 좋아한다", "element": "ELEMENT_METAL"},
            {"question": "남을 불쌍하게 여기고 동정심이 지나치다", "element": "ELEMENT_METAL"},
            {"question": "의욕이 없고 공허함을 잘 느낀다", "element": "ELEMENT_METAL"},
            {"question": "염세적이다", "element": "ELEMENT_METAL"},
            {"question": "죽고 싶은 마음이 잘든다", "element": "ELEMENT_METAL"},
            {"question": "눈물이 많다", "element": "ELEMENT_METAL"},
            {"question": "뒷골이 당기고, 뒷목이 뻐근하다", "element": "ELEMENT_WATER"},
            {"question": "눈알이 뻑뻑하고 빠질것같다", "element": "ELEMENT_WATER"},
            {"question": "귀에 이상(청력이 떨어진다, 귀에서 소리, 가려움증, 중이염,)",
             "element": "ELEMENT_WATER"},
            {"question": "얼굴빛이 윤기가 없고 거무튀튀", "element": "ELEMENT_WATER"},
            {"question": "허리나 등이 아프다", "element": "ELEMENT_WATER"},
            {"question": "발목을 잘 접지른다", "element": "ELEMENT_WATER"},
            {"question": "발바닥이 뜨겁거나 아프다", "element": "ELEMENT_WATER"},
            {"question": "몸이나 종아리가 잘 붓는다", "element": "ELEMENT_WATER"},
            {"question": "몸 여러곳에 염증이 있다 ", "element": "ELEMENT_WATER"},
            {"question": "하품을 잘한다 ", "element": "ELEMENT_WATER"},
            {"question": "소변을 자주본다 ", "element": "ELEMENT_WATER"},
            {"question": "허리가 약하고 자주 삐끗,디스크,요통 ", "element": "ELEMENT_WATER"},
            {"question": "뼈가 약하거나 치아가 좋지않다 ", "element": "ELEMENT_WATER"},
            {"question": "탈모 가있거나 머릿결이 좋지않다 ", "element": "ELEMENT_WATER"},
            {"question": "전립선, 자궁, 생식기 이상 ", "element": "ELEMENT_WATER"},
            {"question": "추위를 많이 탄다 ", "element": "ELEMENT_WATER"},
            {"question": "지구력이 부족해서 꾸준히 하지 못한다 ", "element": "ELEMENT_WATER"},
            {"question": "부정적인 편이고 반대를 잘한다 ", "element": "ELEMENT_WATER"},
            {"question": "늘 피곤하고 쉽게지친다 ", "element": "ELEMENT_WATER"},
            {"question": "열이 올랐다 내렸다 한다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "어깨가 무겁고 결린다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "목에 뭐가 걸린 것 같고 잔기침,헛기침을 잘한다 ",
                "element": "ELEMENT_SANGHWA"},
            {"question": "음식물을 잘 못넘기고 사래에 잘 걸린다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "잘 체하고 명치끝이 답답하다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "미간이 찌푸려지고 표정이 다양하지 않다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "나도 모르게 인상을 쓰고있다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "환절기에 몸이 힘들고 감기나 몸살을 한다 ", "element": "ELEMENT_SANGHWA"},
            {
                "question": "손가락 마디가 굵어지고 손저린증, 손에 허물 벗겨지는등 손에 이상이 있다",
                "element": "ELEMENT_SANGHWA",
            },
            {"question": "다한증, 손이 차고 땀이 많이 난다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "운동신경, 특히 순발력이 떨어진다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "꼬리뼈가 아프다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "틱증상이 있다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "신경이 예민하다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "감정 기복이 심하다 ", "element": "ELEMENT_SANGHWA"},
            {"question": "불안초조 ", "element": "ELEMENT_SANGHWA"},
            {"question": "우울증이 있고 사람 만나는 것이 싫어진다", "element": "ELEMENT_SANGHWA"},
            {"question": "아니꼽고 치사한 일이 많다", "element": "ELEMENT_SANGHWA"},
        ]

        for i in questions:
            CheckListQuestion.objects.create(
                question=i["question"], element=i["element"]
            )
        self.stdout.write(self.style.SUCCESS(
            f"{len(questions)} {NAME} created"))
