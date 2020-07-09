from . import types, models
from graphql_jwt.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


@login_required
def resolve_get_class_list(self, info):
    classes = models.ClassOrder.objects.all()
    return types.GetClassListReponse(classes=classes)


@login_required
def resolve_get_report_list(self, info):
    user = info.context.user
    reports = models.Report.objects.filter(user=user)
    return types.GetReportListResponse(reports=reports)


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
    application = models.Application.objects.get(user=user)
    return types.GetApplicationResponse(application=application)


@login_required
def resolve_get_survey(self, info):
    user = info.context.user
    surveys = models.Survey.objects.filter(user=user)
    return types.GetSurveyResponse(surveys=surveys)
