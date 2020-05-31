# Generated by Django 3.1a1 on 2020-05-31 07:33

from django.db import migrations, models
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckListAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='만들어진 날')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트된 날')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='고유 번호')),
                ('previous_answer', models.BooleanField(default=False, verbose_name='답변 1')),
                ('later_answer', models.BooleanField(default=False, verbose_name='답변 2')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckListQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='만들어진 날')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트된 날')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='고유 번호')),
                ('element', models.CharField(blank=True, choices=[('ELEMENT_WOOD', '목'), ('ELEMENT_FIRE', '화'), ('ELEMENT_EARTH', '토'), ('ELEMENT_METAL', '금'), ('ELEMENT_WATER', '수'), ('ELEMENT_SANGHWA', '상화')], max_length=20, verbose_name='오행')),
                ('question', models.CharField(max_length=5000, verbose_name='질문')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HabitCheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='만들어진 날')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트된 날')),
                ('wakeup_time', models.CharField(max_length=200, verbose_name='기상시간이 규칙적인가요?')),
                ('wakeup_long', models.CharField(max_length=200, verbose_name='하루 몇 시간 정도 주무시나요?')),
                ('wakeup_condition', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('WAKEUP_CONDITION_A', '개운하다'), ('WAKEUP_CONDITION_B', '머리가 아프다'), ('WAKEUP_CONDITION_C', '눈이 아프거나 잘 안 떠진다'), ('WAKEUP_CONDITION_D', '몸이 결리거나 뻐근하다'), ('WAKEUP_CONDITION_E', '일어나기 힘들다'), ('WAKEUP_CONDITION_F', '멍하다'), ('WAKEUP_CONDITION_G', '손이나 발 등이 저리다'), ('WAKEUP_CONDITION_H', '부어있다 (얼굴, 손, 발 등)')], max_length=151, null=True, verbose_name='나는 아침에 일어났을 때...')),
                ('wakeup_condition_etc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='나는 아침에 일어났을 때...(기타)')),
                ('wakeup_first_thing', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('WAKEUP_FIRST_THING_A', '찬물 혹은 찬음료를 마신다'), ('WAKEUP_FIRST_THING_B', '뜨거운 물 혹은 차를 마신다'), ('WAKEUP_FIRST_THING_C', '가벼운 스트레칭'), ('WAKEUP_FIRST_THING_D', '양치, 세수, 샤워'), ('WAKEUP_FIRST_THING_E', '스마트폰'), ('WAKEUP_FIRST_THING_F', '잡지, 신문')], max_length=125, null=True, verbose_name='아침에 눈 떠서 가장 처음에 하는 일은?')),
                ('wakeup_first_thing_etc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='아침에 눈 떠서 가장 처음에 하는 일은?(기타)')),
                ('meal', models.CharField(max_length=3000, verbose_name='하루에 몇 끼, 무엇을, 몇 시에 드시나요?')),
                ('meal_during', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('MEAL_DURING_A', '대화를 많이 하는 편이다'), ('MEAL_DURING_B', '먹는 것에 집중하는 편이다'), ('MEAL_DURING_C', 'TV, 스마트폰 등을 보면서 먹는다'), ('MEAL_DURING_D', '꼭꼭 씹어서 먹는다'), ('MEAL_DURING_E', '급하게 먹는다'), ('MEAL_DURING_F', '많이 먹는다'), ('MEAL_DURING_G', '입이 짧다 (많이 못 먹는다)'), ('MEAL_DURING_H', '음식의 맛을 음미하면서 먹는다'), ('MEAL_DURING_I', '끼니 때우듯 먹는 편이다'), ('MEAL_DURING_J', '식욕이 별로 없다'), ('MEAL_DURING_K', '밥맛이 아주 좋다')], max_length=153, null=True, verbose_name='식사할 때, 나는 주로...')),
                ('meal_during_etc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='식사할 때, 나는 주로...(기타)')),
                ('meal_with_water', models.CharField(choices=[('DEGREE_A', '안한다'), ('DEGREE_B', '거의 안한다'), ('DEGREE_C', '가끔 한다'), ('DEGREE_D', '자주 한다'), ('DEGREE_E', '매일 한다')], max_length=300, verbose_name='식사 전후에 물을 많이 마시나요?')),
                ('meal_with_snack', models.CharField(choices=[('DEGREE_A', '안한다'), ('DEGREE_B', '거의 안한다'), ('DEGREE_C', '가끔 한다'), ('DEGREE_D', '자주 한다'), ('DEGREE_E', '매일 한다')], max_length=300, verbose_name='식사 외에 간식, 군것질을 하시나요?')),
                ('meal_with_night_food', models.CharField(choices=[('DEGREE_A', '안한다'), ('DEGREE_B', '거의 안한다'), ('DEGREE_C', '가끔 한다'), ('DEGREE_D', '자주 한다'), ('DEGREE_E', '매일 한다')], max_length=300, verbose_name='야식을 많이 드시나요? ')),
                ('after_lunch', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('AFTER_LUNCH_A', '스마트폰을 본다'), ('AFTER_LUNCH_B', '밖에 나가 걷거나 산책을 한다'), ('AFTER_LUNCH_C', '담배를 핀다'), ('AFTER_LUNCH_D', '커피 등 후식을 즐긴다'), ('AFTER_LUNCH_E', '수다를 즐긴다'), ('AFTER_LUNCH_F', '잠이 쏟아진다')], max_length=83, null=True, verbose_name='점심식사 후 나는 주로...')),
                ('after_lunch_etc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='점심식사 후 나는 주로...(기타)')),
                ('saying', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('SAYING_A', '말의 속도가 빠르다'), ('SAYING_B', '듣는 것보다 말하는 것에 더 익숙하다'), ('SAYING_C', '상대방의 말을 잘 듣는 편이다'), ('SAYING_D', '말을 자주 더듬는다'), ('SAYING_E', '말을 거침없이 한다'), ('SAYING_F', '자주 흥분해서 말한다'), ('SAYING_G', '말이 별로 없다'), ('SAYING_H', '생각을 하고 말을 하는 편이다'), ('SAYING_I', '말을 하면서 생각하는 편이다'), ('SAYING_J', '말실수를 많이 한다'), ('SAYING_K', '부정적인 반응을 자주 보인다(아닌 것 같은데~ 등)')], max_length=98, null=True, verbose_name='내가 말을 할 때...')),
                ('saying_etc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='나내가 말을 할 때...(기타)')),
                ('saying_repeat', models.CharField(max_length=2000, verbose_name='내가 말할 때 가장 자주 쓰는 말은?')),
                ('walking', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('WALKING_A', '걸음이 느리다'), ('WALKING_B', '걸음이 빠른 편이다'), ('WALKING_C', '옆사람과 나란히 걷는다'), ('WALKING_D', '앞서서 걷는 편이다'), ('WALKING_E', '발을 끌면서 걷는다'), ('WALKING_F', '허리가 굽어 있다'), ('WALKING_G', '파워워킹을 한다'), ('WALKING_H', '오래 걷지 못한다')], max_length=79, null=True, verbose_name='나는 걸을 때...')),
                ('walking_etc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='나는 걸을 때...(기타)')),
                ('posture', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('POSTURE_A', '앉아 있는 시간'), ('POSTURE_B', '서 있는 시간'), ('POSTURE_C', '걷는 시간'), ('POSTURE_D', '교통수단을 이용하는 시간'), ('POSTURE_E', '누워 있는 시간')], max_length=49, null=True, verbose_name='하루 중 어느 시간이 가장 긴가요?')),
                ('posture_etc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='하루 중 어느 시간이 가장 긴가요?(기타)')),
                ('posture_detail', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('POSTURE_DETAIL_A', '자세를 편하게 잘 펴고 있다'), ('POSTURE_DETAIL_B', '자세가 무너져 있다'), ('POSTURE_DETAIL_C', '앉아 있는 것에 익숙하다'), ('POSTURE_DETAIL_D', '오래 서 있지 못한다'), ('POSTURE_DETAIL_E', '앉아 있는 게 힘들다'), ('POSTURE_DETAIL_F', '등이 굽어 있거나 거북목이다'), ('POSTURE_DETAIL_G', '일자목, 목이 돌아가지 않는다'), ('POSTURE_DETAIL_H', '다리를 자주 꼰다'), ('POSTURE_DETAIL_I', '무지외반증이 있다'), ('POSTURE_DETAIL_J', '다리가 휘어 있다 (안으로, 밖으로 등)')], max_length=169, null=True, verbose_name='나의 평소 자세는?')),
                ('posture_detail_etc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='나의 평소 자세는?(기타)')),
                ('body_heat', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('BODY_HEAT_A', '열이 많아서 옷을 얇게 입는다'), ('BODY_HEAT_B', '찬물을 피한다'), ('BODY_HEAT_C', '찬물을 즐겨 마신다'), ('BODY_HEAT_D', '뜨거운 차를 자주 마신다'), ('BODY_HEAT_E', '핫팩을 자주 붙이고 다닌다'), ('BODY_HEAT_F', '목도리, 장갑 등을 챙겨서 한다'), ('BODY_HEAT_G', '내의를 챙겨 입는다'), ('BODY_HEAT_H', '발을 항상 따듯하게 해 준다'), ('BODY_HEAT_I', '발이 답답해서 집에서 맨발로 다닌다'), ('BODY_HEAT_J', '찜질팩, 돌뜸 등을 늘 챙겨서 한다'), ('BODY_HEAT_K', '족탕, 반신욕, 찜질 등을 한다')], max_length=131, null=True, verbose_name='체온조절을 위해 어떤 일을 하고 계시나요?')),
                ('body_heat_etc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='체온조절을 위해 어떤 일을 하고 계시나요?(기타)')),
                ('exercise', models.CharField(max_length=2000, verbose_name='지금 하고 있는 운동이 있으신가요?')),
                ('sleeping', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('SLEEPING_A', '머리를 대면 바로 잠든다'), ('SLEEPING_B', '한참을 뒤척이다 자야 한다'), ('SLEEPING_C', '새벽에 꼭 한 번(이상) 일어난다'), ('SLEEPING_D', '잠을 못 잔다')], max_length=43, null=True, verbose_name='잠은 어떻게 주무시나요?')),
                ('sleeping_etc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='잠은 어떻게 주무시나요?(기타)')),
                ('before_sleeping', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('BEFORE_SLEEPING_A', '스마트폰'), ('BEFORE_SLEEPING_B', 'TV시청'), ('BEFORE_SLEEPING_C', '책, 잡지, 신문 등 읽기'), ('BEFORE_SLEEPING_D', '일기, 글쓰기'), ('BEFORE_SLEEPING_E', '야식')], max_length=89, null=True, verbose_name='자기 전 주로 하는 일은?')),
                ('before_sleeping_etc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='자기 전 주로 하는 일은?(기타)')),
                ('good_thing', models.CharField(max_length=2000, verbose_name='나의 좋은 습관은 무엇인가요?')),
                ('bad_thing', models.CharField(max_length=2000, verbose_name='나의 고치고 싶은 습관은 무엇인가요?')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
