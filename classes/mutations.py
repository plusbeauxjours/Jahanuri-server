import graphene
from graphql_jwt.decorators import login_required
from . import types, models


class CreateClassOrder(graphene.Mutation):
    class Arguments:
        order = graphene.Int(required=True)
        start_date = graphene.Date(required=True)
        end_date = graphene.Date(required=True)

    Output = types.CreateClassOrderResponse

    @login_required
    def mutate(self, info, **kwargs):
        order = kwargs.get("order")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")

        class_order = models.ClassOrder.objects.create(
            order=order, start_date=start_date, end_date=end_date
        )

        return types.CreateClassOrderResponse(ok=True)


class UpdateClassOrder(graphene.Mutation):
    class Arguments:
        order_id = graphene.String(required=True)
        order = graphene.Int()
        start_date = graphene.Date()
        end_date = graphene.Date()

    Output = types.UpdateClassOrderResponse

    @login_required
    def mutate(self, info, **kwargs):
        order_id = kwargs.get("order_id")
        order = kwargs.get("order", "")
        start_date = kwargs.get("start_date", "")
        end_date = kwargs.get("end_date", "")

        class_order = models.ClassOrder.objects.get(pk=order_id)

        if order != "":
            class_order.order = order
        if start_date != "":
            class_order.start_date = start_date
        if end_date != "":
            class_order.end_date = end_date

        class_order.save()

        return types.UpdateClassOrderResponse(ok=True)


class RemoveClassOrder(graphene.Mutation):
    class Arguments:
        order_id = graphene.String(required=True)

    Output = types.RemoveClassOrderResponse

    @login_required
    def mutate(self, info, **kwargs):
        order_id = kwargs.get("order_id")
        class_order = models.ClassOrder.objects.get(id=order_id)
        class_order.delete()

        return types.RemoveClassOrderResponse(ok=True)


class CreateReportCover(graphene.Mutation):
    class Arguments:
        order_id = graphene.String(required=True)
        report_type = graphene.String()

    Output = types.CreateReportCoverResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        order_id = kwargs.get("order_id")
        report_type = kwargs.get("report_type", "body study")
        class_order = models.ClassOrder.objects.get(id=order_id)
        report_cover = models.ReportCover.objects.create(
            class_order=class_order, user=user, report_type=report_type
        )

        return types.CreateReportCoverResponse(ok=True)


class UpdateReportCover(graphene.Mutation):
    class Arguments:
        report_uuid = graphene.String(required=True)
        report_type = graphene.String()

    Output = types.UpdateReportCoverResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        report_uuid = kwargs.get("report_uuid")
        report_type = kwargs.get("report_type", "")
        report_cover = models.ReportCover.objects.get(uuid=report_uuid)

        if report_type != "":
            report_cover.report_type = report_type

        report_cover.save()

        return types.UpdateReportCoverResponse(ok=True)


class RemoveReportCover(graphene.Mutation):
    class Arguments:
        report_uuid = graphene.String(required=True)

    Output = types.RemoveReportCoverResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        report_uuid = kwargs.get("report_uuid")
        report_cover = models.ReportCover.objects.get(uuid=report_uuid)

        report_cover.delete()

        return types.RemoveReportCoverResponse(ok=True)


class CreateReport(graphene.Mutation):
    class Arguments:
        report_cover_uuid = graphene.String(required=True)
        saeng_sik = graphene.String()
        amino = graphene.String()
        sangi_so = graphene.String()
        jeun_hae_jil = graphene.Boolean()
        jeun_hae_jil_time = graphene.Time()
        meal = graphene.String()
        meal_check = graphene.String()
        sleeping = graphene.String()
        stool = graphene.String()
        hot_grain = graphene.String()
        hot_water = graphene.String()
        strolling = graphene.String()
        workout = graphene.String()
        lecture = graphene.String()
        etc = graphene.String()
        diary = graphene.String()

    Output = types.CreateReportResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        report_cover_uuid = kwargs.get("report_cover_uuid")
        saeng_sik = kwargs.get("saeng_sik")
        amino = kwargs.get("amino")
        sangi_so = kwargs.get("sangi_so")
        jeun_hae_jil = kwargs.get("jeun_hae_jil")
        jeun_hae_jil_time = kwargs.get("jeun_hae_jil_time")
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
        report_cover = models.ReportCover.objects.get(uuid=report_cover_uuid)
        report = models.Report.objects.create(
            report_cover=report_cover,
            saeng_sik=saeng_sik,
            amino=amino,
            sangi_so=sangi_so,
            jeun_hae_jil=jeun_hae_jil,
            jeun_hae_jil_time=jeun_hae_jil_time,
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


class UpdateReport(graphene.Mutation):
    class Arguments:
        report_uuid = graphene.String(required=True)
        saeng_sik = graphene.String()
        amino = graphene.String()
        sangi_so = graphene.String()
        jeun_hae_jil = graphene.Boolean()
        jeun_hae_jil_time = graphene.Time()
        meal = graphene.String()
        meal_check = graphene.String()
        sleeping = graphene.String()
        stool = graphene.String()
        hot_grain = graphene.String()
        hot_water = graphene.String()
        strolling = graphene.String()
        workout = graphene.String()
        lecture = graphene.String()
        etc = graphene.String()
        diary = graphene.String()

    Output = types.UpdateReportResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        report_uuid = kwargs.get("report_uuid", "")
        saeng_sik = kwargs.get("saeng_sik", "")
        amino = kwargs.get("amino", "")
        sangi_so = kwargs.get("sangi_so", "")
        jeun_hae_jil = kwargs.get("jeun_hae_jil", False)
        jeun_hae_jil_time = kwargs.get("jeun_hae_jil_time", "")
        meal = kwargs.get("meal", "")
        meal_check = kwargs.get("meal_check", "")
        sleeping = kwargs.get("sleeping", "")
        stool = kwargs.get("stool", "")
        hot_grain = kwargs.get("hot_grain", "")
        hot_water = kwargs.get("hot_water", "")
        strolling = kwargs.get("strolling", "")
        workout = kwargs.get("workout", "")
        lecture = kwargs.get("lecture", "")
        etc = kwargs.get("etc", "")
        diary = kwargs.get("diary", "")
        report = models.Report.objects.get(uuid=report_uuid)

        if saeng_sik != "":
            report.saeng_sik = saeng_sik
        if amino != "":
            report.amino = amino
        if sangi_so != "":
            report.sangi_so = sangi_so
        if jeun_hae_jil != "":
            report.jeun_hae_jil = jeun_hae_jil
        if jeun_hae_jil_time != "":
            report.jeun_hae_jil_time = jeun_hae_jil_time
        if meal != "":
            report.meal = meal
        if meal_check != "":
            report.meal_check = meal_check
        if sleeping != "":
            report.sleeping = sleeping
        if stool != "":
            report.stool = stool
        if hot_grain != "":
            report.hot_grain = hot_grain
        if hot_water != "":
            report.hot_water = hot_water
        if strolling != "":
            report.strolling = strolling
        if workout != "":
            report.workout = workout
        if lecture != "":
            report.lecture = lecture
        if etc != "":
            report.etc = etc
        if diary != "":
            report.diary = diary

        report.save()
        return types.UpdateReportResponse(report=report)


class RemoveReport(graphene.Mutation):
    class Arguments:
        report_uuid = graphene.String(required=True)

    Output = types.RemoveReportResponse

    @login_required
    def mutate(self, info, **kwargs):
        report_uuid = kwargs.get("report_uuid")
        report = models.Report.objects.get(uuid=report_uuid)
        report.delete()

        return types.RemoveReportResponse(ok=True)
