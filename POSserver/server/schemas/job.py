from graphene import relay, List, ObjectType
import graphene
from graphene_django import DjangoObjectType
from server.models import Job
from graphene_django.filter import DjangoFilterConnectionField


class Job_Type(DjangoObjectType):
    class Meta:
        model = Job
        filter_fields = [
            "id",
            "client",
            "name",
            "complete",
            "labor",
            "description",
            "created_at",
            "modified_at",
            "deadline",
        ]
        interfaces = (relay.Node,)


class Query(ObjectType):
    jobs = List(Job_Type)
    all_jobs = DjangoFilterConnectionField(Job_Type)

    def resolve_jobs(self, info, **kwargs):
        user = info.context.user

        if user.is_anonymous:
            return Job.objects.none()
        else:
            return Job.objects.filter(user=user)


class CreateJob(graphene.Mutation):
    class Arguments:
        clientId = graphene.ID()
        complete = graphene.Boolean()
        name = graphene.String()
        labor = graphene.Float(2)
        description = graphene.String()
        createdAt = graphene.types.datetime.DateTime()
        modifiedAt = graphene.types.datetime.DateTime()
        deadline = graphene.types.datetime.Date()

    ok = graphene.Boolean()
    job = graphene.Field(Job_Type)

    def mutate(
        self,
        info,
        clientId,
        name,
        labor,
        description,
        complete,
        createdAt,
        modifiedAt,
        deadline,
    ):
        user = info.context.user
        if user.is_anonymous:
            return CreateJob(ok=False, status="Must be logged in.")
        else:
            new_job = Job(
                client_id=clientId,
                name=name,
                description=description,
                labor=labor,
                complete=complete,
                created_at=createdAt,
                modified_at=modifiedAt,
                deadline=deadline,
            )
            new_job.save()
            return CreateJob(job=new_job, ok=True)


class JobMutation(graphene.ObjectType):
    create_job = CreateJob.Field()
