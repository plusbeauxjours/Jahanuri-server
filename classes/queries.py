from . import types, models
from graphql_jwt.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


@login_required
def resolve_get_class_list(self, info):
    classes = models.ClassOrder.objects.all()
    return types.GetClassListReponse(classes=classes)


@login_required
def resolve_get_report_cover_list(self, info, **kwargs):
    class_order_id = kwargs.get("class_order_id", "")

    if class_order_id != "":
        report_covers = models.ReportCover.objects.filter(
            class_order__pk__in=class_order_id
        )
        return types.GetReportCoverListResponse(report=report_covers)
    else:
        return types.GetReportCoverListResponse(reportCovers=None)


@login_required
def resolve_get_report_list(self, info, **kwargs):
    class_order_id = kwargs.get("class_order_id", "")
    user_uuid = kwargs.get("user_uuid", "")

    if class_order_id != "":
        report_covers = models.ReportCover.objects.filter(
            class_order__pk__in=class_order_id
        ).order_by("-report_date")
        return types.GetReportCoverListResponse(reportCovers=report_covers)
    elif user_uuid != "":
        reports = models.Report.objects.filter(
            report_cover__user__uuid=user_uuid
        ).order_by("-report_date")
        return types.GetReportListResponse(reports=reports)
    else:
        return types.GetReportListResponse(reports=None)


@login_required
def resolve_get_report_detail(self, info, **kwargs):
    report_uuid = kwargs.get("report_uuid")
    try:
        report = models.Report.objects.get(uuid=report_uuid)
        return types.GetReportDetailResponse(report=report)
    except models.Report.DoesNotExist:
        return types.GetReportDetailResponse(report=None)


@login_required
def resolve_get_application(self, info):
    user = info.context.user
    try:
        application = user.application
        return types.GetApplicationResponse(application=application)
    except ObjectDoesNotExist:
        return types.GetApplicationResponse(application=None)


@login_required
def resolve_get_survey(self, info):
    user = info.context.user
    try:
        survey = user.survey
        return types.GetSurveyResponse(survey=survey)
    except ObjectDoesNotExist:
        return types.GetSurveyResponse(survey=None)
