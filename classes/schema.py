import graphene
from . import types, queries, mutations


class Query(object):
    get_class_list = graphene.Field(
        types.GetClassListReponse,
        resolver=queries.resolve_get_class_list,
        required=True,
    )
    get_report_list = graphene.Field(
        types.GetReportListResponse,
        resolver=queries.resolve_get_report_list,
        required=True,
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
    get_survey = graphene.Field(
        types.GetSurveyResponse, resolver=queries.resolve_get_survey, required=True,
    )


class Mutation(object):
    create_report = mutations.CreateReport.Field(required=True)
    # update_report = mutations.UpdateReport.Field(required=True)
    # remove_report = mutations.RemoveReport.Field(required=True)
    submit_application = mutations.SubmitApplication.Field(required=True)
    submit_survey = mutations.SubmitSurvey.Field(required=True)
