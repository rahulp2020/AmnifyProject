import graphene
from graphene_django.types import DjangoObjectType
from .model.appointment import Appointment


class AppointmentsType(DjangoObjectType):
    class Meta:
        model = Appointment
        fields = ("id", "name", "time", "status", "address", "created_at", "updated_at")


class Query(graphene.ObjectType):
    all_appointments = graphene.List(AppointmentsType)

    def resolve_all_appointments(root, info):
        return Appointment.objects.all()


class CreateAppointment(graphene.Mutation):
    class Arguments:
        time = graphene.DateTime(required=True)
        name = graphene.String(required=True)
        address = graphene.String(required=True)

    appointment = graphene.Field(AppointmentsType)

    def mutate(root, info, time,name,address):
        appointment = Appointment.objects.create(time=time,name=name,address=address, status='Booked')
        return CreateAppointment(appointment=appointment)


class CancelAppointment(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(root, info, id):
        try:
            appointment = Appointment.objects.get(id=id)
            appointment.status = "Cancelled"
            appointment.save()
            return CancelAppointment(success=True)
        except Appointment.DoesNotExist:
            return CancelAppointment(success=False)


class Mutation(graphene.ObjectType):
    create_appointment = CreateAppointment.Field()
    cancel_appointment = CancelAppointment.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
