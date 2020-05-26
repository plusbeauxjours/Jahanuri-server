import graphene
from . import types, queries, mutations


class Query(object):
    get_class_list = graphene.Field(
        types.GetClassListReponse,
        resolver=queries.resolve_get_class_list,
        required=True,
    )
    get_report_cover_list = graphene.Field(
        types.GetReportCoverListResponse,
        resolver=queries.resolve_get_report_cover_list,
        required=True,
        args={"class_order_id": graphene.String(),},
    )
    get_report_list = graphene.Field(
        types.GetReportListResponse,
        resolver=queries.resolve_get_report_list,
        required=True,
        args={"class_order_id": graphene.String(), "user_uuid": graphene.String(),},
    )
    get_report_detail = graphene.Field(
        types.GetReportDetailResponse,
        resolver=queries.resolve_get_report_detail,
        required=True,
        args={"report_uuid": graphene.String()},
    )
    get_application = graphene.Field(
        types.GetApplicationResponse,
        resolver=queries.resolve_get_application,
        required=True,
    )


class Mutation(object):
    # create_class_order = mutations.CreateClassOrder.Field(required=True)
    # update_class_order = mutations.UpdateClassOrder.Field(required=True)
    # remove_class_order = mutations.RemoveClassOrder.Field(required=True)
    # create_report_cover = mutations.CreateReportCover.Field(required=True)
    # update_report_cover = mutations.UpdateReportCover.Field(required=True)
    # remove_report_cover = mutations.RemoveReportCover.Field(required=True)
    create_report = mutations.CreateReport.Field(required=True)
    # update_report = mutations.UpdateReport.Field(required=True)
    # remove_report = mutations.RemoveReport.Field(required=True)
    submit_application = mutations.SubmitApplication.Field(required=True)
