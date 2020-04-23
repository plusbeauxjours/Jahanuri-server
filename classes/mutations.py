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
        order_id = graphene.String()
        report_uuid = graphene.String(required=True)
        report_type = graphene.String()

    Output = types.UpdateReportCoverResponse

    @login_required
    def mutate(self, info, **kwargs):
        user = info.context.user
        report_uuid = kwargs.get("report_uuid")
        order_id = kwargs.get("order_id", "")
        report_type = kwargs.get("report_type", "")
        class_order = models.ClassOrder.objects.get(id=order_id)
        report_cover = models.ReportCover.objects.get(uuid=report_uuid)

        if order_id != "":
            report_cover.class_order = class_order

        if report_type != "":
            report_cover.report_type = report_type

        report_cover.save()

        return types.UpdateReportCoverResponse(ok=True)
