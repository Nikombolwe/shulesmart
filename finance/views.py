from rest_framework.permissions import IsAuthenticated
from core.views import TenantScopedViewSet
from .models import FeeStructure, Invoice, Payment
from .serializers import FeeStructureSerializer, InvoiceSerializer, PaymentSerializer

class FeeStructureViewSet(TenantScopedViewSet):
    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)


class InvoiceViewSet(TenantScopedViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(school=self.request.user.school)


class PaymentViewSet(TenantScopedViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save(school=self.request.user.school)
        
        # Mantiki ya kusasisha kiasi kilicholipwa (paid_amount) na status ya Invoice kiutomatiki
        invoice = payment.invoice
        invoice.paid_amount += payment.amount_paid
        
        if invoice.paid_amount >= invoice.total_amount:
            invoice.status = 'PAID'
        elif invoice.paid_amount > 0:
            invoice.status = 'PARTIAL'
            
        invoice.save()