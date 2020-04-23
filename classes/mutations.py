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
        order = kwargs.get("order")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")

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
