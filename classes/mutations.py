import graphene
from graphql_jwt.decorators import login_required
from . import types, models


class CreateReport(graphene.Mutation):
    class Arguments:
        saeng_sik_morning = graphene.String()
        saeng_sik_noon = graphene.String()
        saeng_sik_evening = graphene.String()
        amino_morning = graphene.String()
        amino_noon = graphene.String()
        amino_evening = graphene.String()
        sangi_so_morning = graphene.String()
        sangi_so_noon = graphene.String()
        sangi_so_evening = graphene.String()
        jeun_hae_jil_a = graphene.Boolean()
        jeun_hae_jil_b = graphene.Boolean()
        jeun_hae_jil_c = graphene.Boolean()
        jeun_hae_jil_d = graphene.Boolean()
        meal = graphene.String(required=True)
        meal_check = graphene.String(required=True)
        sleeping = graphene.String(required=True)
        stool = graphene.String(required=True)
        hot_grain = graphene.String(required=True)
        hot_water = graphene.String(required=True)
        strolling = graphene.String(required=True)
        workout = graphene.String(required=True)
        lecture = graphene.String(required=True)
        etc = graphene.String(required=True)
        diary = graphene.String(required=True)
        report_date = graphene.types.datetime.DateTime(required=True)

    Output = types.CreateReportResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        saeng_sik_morning = kwargs.get("saeng_sik_morning")
        saeng_sik_noon = kwargs.get("saeng_sik_noon")
        saeng_sik_evening = kwargs.get("saeng_sik_evening")
        amino_morning = kwargs.get("amino_morning")
        amino_noon = kwargs.get("amino_noon")
        amino_evening = kwargs.get("amino_evening")
        sangi_so_morning = kwargs.get("sangi_so_morning")
        sangi_so_noon = kwargs.get("sangi_so_noon")
        sangi_so_evening = kwargs.get("sangi_so_evening")
        jeun_hae_jil_a = kwargs.get("jeun_hae_jil_a")
        jeun_hae_jil_b = kwargs.get("jeun_hae_jil_b")
        jeun_hae_jil_c = kwargs.get("jeun_hae_jil_c")
        jeun_hae_jil_d = kwargs.get("jeun_hae_jil_d")
        meal = kwargs.get("meal")
        meal_check = kwargs.get("meal_check")
        sleeping = kwargs.get("sleeping")
        stool = kwargs.get("stool")
        hot_grain = kwargs.get("hot_grain")
        hot_water = kwargs.get("hot_water")
        strolling = kwargs.get("strolling")
        workout = kwargs.get("workout")
        lecture = kwargs.get("lecture")
        etc = kwargs.get("etc")
        diary = kwargs.get("diary")
        report_date = kwargs.get("report_date")

        if user.has_paid and user.class_order:
            class_order = user.class_order
            report = models.Report.objects.create(
                user=user,
                report_date=report_date,
                class_order=class_order,
                saeng_sik_morning=saeng_sik_morning,
                saeng_sik_noon=saeng_sik_noon,
                saeng_sik_evening=saeng_sik_evening,
                amino_morning=amino_morning,
                amino_noon=amino_noon,
                amino_evening=amino_evening,
                sangi_so_morning=sangi_so_morning,
                sangi_so_noon=sangi_so_noon,
                sangi_so_evening=sangi_so_evening,
                jeun_hae_jil_a=jeun_hae_jil_a,
                jeun_hae_jil_b=jeun_hae_jil_b,
                jeun_hae_jil_c=jeun_hae_jil_c,
                jeun_hae_jil_d=jeun_hae_jil_d,
                meal=meal,
                meal_check=meal_check,
                sleeping=sleeping,
                stool=stool,
                hot_grain=hot_grain,
                hot_water=hot_water,
                strolling=strolling,
                workout=workout,
                lecture=lecture,
                etc=etc,
                diary=diary,
            )
            return types.CreateReportResponse(report=report)

        else:
            report = models.Report.objects.create(
                report_date=report_date,
                class_order=None,
                saeng_sik_morning=saeng_sik_morning,
                saeng_sik_noon=saeng_sik_noon,
                saeng_sik_evening=saeng_sik_evening,
                amino_morning=amino_morning,
                amino_noon=amino_noon,
                amino_evening=amino_evening,
                sangi_so_morning=sangi_so_morning,
                sangi_so_noon=sangi_so_noon,
                sangi_so_evening=sangi_so_evening,
                jeun_hae_jil_a=jeun_hae_jil_a,
                jeun_hae_jil_b=jeun_hae_jil_b,
                jeun_hae_jil_c=jeun_hae_jil_c,
                jeun_hae_jil_d=jeun_hae_jil_d,
                meal=meal,
                meal_check=meal_check,
                sleeping=sleeping,
                stool=stool,
                hot_grain=hot_grain,
                hot_water=hot_water,
                strolling=strolling,
                workout=workout,
                lecture=lecture,
                etc=etc,
                diary=diary,
            )
            return types.CreateReportResponse(report=report)


# class UpdateReport(graphene.Mutation):
#     class Arguments:
#         saeng_sik_morning = graphene.String()
#         saeng_sik_noon = graphene.String()
#         saeng_sik_evening = graphene.String()
#         amino_morning = graphene.String()
#         amino_noon = graphene.String()
#         amino_evening = graphene.String()
#         sangi_so_morning = graphene.String()
#         sangi_so_noon = graphene.String()
#         sangi_so_evening = graphene.String()
#         jeun_hae_jil_a = graphene.Boolean()
#         jeun_hae_jil_b = graphene.Boolean()
#         jeun_hae_jil_c = graphene.Boolean()
#         jeun_hae_jil_d = graphene.Boolean()
#         meal = graphene.String(required=True)
#         meal_check = graphene.String(required=True)
#         sleeping = graphene.String(required=True)
#         stool = graphene.String(required=True)
#         hot_grain = graphene.String(required=True)
#         hot_water = graphene.String(required=True)
#         strolling = graphene.String(required=True)
#         workout = graphene.String(required=True)
#         lecture = graphene.String(required=True)
#         etc = graphene.String(required=True)
#         diary = graphene.String(required=True)
#         report_date = graphene.Date(required=True)

#     Output = types.UpdateReportResponse

#     @login_required
#     def mutate(self, info, **kwargs):
#         user = info.context.user
#         report_uuid = kwargs.get("report_uuid", "")
#         saeng_sik_morning = kwargs.get("saeng_sik_morning", "")
#         saeng_sik_noon = kwargs.get("saeng_sik_noon", "")
#         saeng_sik_evening = kwargs.get("saeng_sik_evening", "")
#         amino_morning = kwargs.get("amino_morning", "")
#         amino_noon = kwargs.get("amino_noon", "")
#         amino_evening = kwargs.get("amino_evening", "")
#         sangi_so_morning = kwargs.get("sangi_so_morning", "")
#         sangi_so_noon = kwargs.get("sangi_so_noon", "")
#         sangi_so_evening = kwargs.get("sangi_so_evening", "")
#         jeun_hae_jil_a = kwargs.get("jeun_hae_jil_a", False)
#         jeun_hae_jil_b = kwargs.get("jeun_hae_jil_b", False)
#         jeun_hae_jil_c = kwargs.get("jeun_hae_jil_c", False)
#         jeun_hae_jil_d = kwargs.get("jeun_hae_jil_d", False)
#         meal = kwargs.get("meal", "")
#         meal_check = kwargs.get("meal_check", "")
#         sleeping = kwargs.get("sleeping", "")
#         stool = kwargs.get("stool", "")
#         hot_grain = kwargs.get("hot_grain", "")
#         hot_water = kwargs.get("hot_water", "")
#         strolling = kwargs.get("strolling", "")
#         workout = kwargs.get("workout", "")
#         lecture = kwargs.get("lecture", "")
#         etc = kwargs.get("etc", "")
#         diary = kwargs.get("diary", "")
#         report_date = kwargs.get("report_date", "")
#         report = models.Report.objects.get(uuid=report_uuid)

#         if report_date != "":
#             report.report_date = report_date
#         if saeng_sik_morning != "":
#             report.saeng_sik_morning = saeng_sik_morning
#         if saeng_sik_noon != "":
#             report.saeng_sik_noon = saeng_sik_noon
#         if saeng_sik_evening != "":
#             report.saeng_sik_evening = saeng_sik_evening
#         if amino_morning != "":
#             report.amino_morning = amino_morning
#         if amino_noon != "":
#             report.amino_noon = amino_noon
#         if amino_evening != "":
#             report.amino_evening = amino_evening
#         if sangi_so_morning != "":
#             report.sangi_so_morning = sangi_so_morning
#         if sangi_so_noon != "":
#             report.sangi_so_noon = sangi_so_noon
#         if sangi_so_evening != "":
#             report.sangi_so_evening = sangi_so_evening
#         if jeun_hae_jil_a != "":
#             report.jeun_hae_jil_a = jeun_hae_jil_a
#         if jeun_hae_jil_b != "":
#             report.jeun_hae_jil_b = jeun_hae_jil_b
#         if jeun_hae_jil_c != "":
#             report.jeun_hae_jil_c = jeun_hae_jil_c
#         if jeun_hae_jil_d != "":
#             report.jeun_hae_jil_d = jeun_hae_jil_d
#         if meal != "":
#             report.meal = meal
#         if meal_check != "":
#             report.meal_check = meal_check
#         if sleeping != "":
#             report.sleeping = sleeping
#         if stool != "":
#             report.stool = stool
#         if hot_grain != "":
#             report.hot_grain = hot_grain
#         if hot_water != "":
#             report.hot_water = hot_water
#         if strolling != "":
#             report.strolling = strolling
#         if workout != "":
#             report.workout = workout
#         if lecture != "":
#             report.lecture = lecture
#         if etc != "":
#             report.etc = etc
#         if diary != "":
#             report.diary = diary

#         report.save()
#         return types.UpdateReportResponse(report=report)


# class RemoveReport(graphene.Mutation):
#     class Arguments:
#         report_uuid = graphene.String(required=True)

#     Output = types.RemoveReportResponse

#     @login_required
#     def mutate(self, info, **kwargs):
#         report_uuid = kwargs.get("report_uuid")
#         report = models.Report.objects.get(uuid=report_uuid)
#         report.delete()

#         return types.RemoveReportResponse(ok=True)


class SubmitApplication(graphene.Mutation):
    class Arguments:
        gender = graphene.String(required=True)
        birth_date = graphene.types.datetime.DateTime()
        address = graphene.String(required=True)
        job = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        email_address = graphene.String(required=True)
        approach = graphene.List(graphene.String)
        approach_etc = graphene.String()
        confirm = graphene.Boolean(required=True)

    Output = types.SubmitApplicationResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        gender = kwargs.get("gender", "")
        birth_date = kwargs.get("birth_date", "")
        address = kwargs.get("address", "")
        job = kwargs.get("job", "")
        phone_number = kwargs.get("phone_number", "")
        email_address = kwargs.get("email_address", "")
        approach = kwargs.get("approach", [])
        approach_etc = kwargs.get("approach_etc", "")
        confirm = kwargs.get("confirm")

        newApplication = models.Application.objects.create(
            user=user,
            gender=gender,
            birth_date=birth_date,
            address=address,
            job=job,
            phone_number=phone_number,
            email_address=email_address,
            approach=approach,
            approach_etc=approach_etc,
            confirm=confirm,
        )

        if gender != "":
            user.gender = gender
        if birth_date != "":
            user.birth_date = birth_date
        if address != "":
            user.address = address
        if job != "":
            user.job = job
        if phone_number != "":
            user.phone_number = phone_number
        if email_address != "":
            user.email = email_address
        if approach != []:
            user.approach = approach
        if approach_etc != "":
            user.approach_etc = approach_etc
        user.has_submitted_application = True
        user.save()
        return types.SubmitApplicationResponse(ok=True)


class SubmitSurvey(graphene.Mutation):
    class Arguments:
        has_married = graphene.Boolean(required=True)
        has_married_etc = graphene.String()
        has_childbirth = graphene.Boolean(required=True)
        has_childbirth_etc = graphene.String()
        status = graphene.String(required=True)
        change = graphene.String(required=True)
        agree_personal_information = graphene.Boolean(required=True)
        confirm = graphene.Boolean(required=True)

    Output = types.SubmitSurveyResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        has_married = kwargs.get("has_married", False)
        has_married_etc = kwargs.get("has_married_etc", "")
        has_childbirth = kwargs.get("has_childbirth", False)
        has_childbirth_etc = kwargs.get("has_childbirth_etc", "")
        status = kwargs.get("status", "")
        change = kwargs.get("change", "")
        agree_personal_information = kwargs.get(
            "agree_personal_information", False)
        confirm = kwargs.get("confirm", False)

        newSurvey = models.Survey.objects.create(
            user=user,
            has_married=has_married,
            has_married_etc=has_married_etc,
            has_childbirth=has_childbirth,
            has_childbirth_etc=has_childbirth_etc,
            status=status,
            change=change,
            agree_personal_information=agree_personal_information,
            confirm=confirm,
        )

        if has_married != False:
            user.has_married = has_married
        if has_married_etc != "":
            user.has_married_etc = has_married_etc
        if has_childbirth != False:
            user.has_childbirth = has_childbirth
        if has_childbirth_etc != "":
            user.has_childbirth_etc = has_childbirth_etc

        user.has_submitted_survey = True
        user.save()
        return types.SubmitSurveyResponse(ok=True)
