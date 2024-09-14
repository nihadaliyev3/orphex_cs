from rest_framework.response import Response
from rest_framework.views import APIView
from .services import calculate_conversion_rate, status_based_analysis, load_data, category_type_performance, filtered_aggregation


class ConversionRateView(APIView):
    def get(self, request):
        df = load_data()
        rates, highest, lowest = calculate_conversion_rate(df)

        return Response({
            "conversion_rates": rates.to_dict(orient='records'),
            "highest": highest.to_dict(),
            "lowest": lowest.to_dict()
        })


class StatusDistributionView(APIView):
    def get(self, request):
        df = load_data()
        distribution, revenue_conversions_by_status = status_based_analysis(df)

        return Response({
            "status_distribution": distribution.to_dict(orient='records'),
            "revenue_conversions_by_status": revenue_conversions_by_status.to_dict(orient='records')
        })


class CategoryTypePerformanceView(APIView):
    def get(self, request):
        df = load_data()
        performance_data, top_combination = category_type_performance(df)
        performance_data = performance_data.to_dict(orient='records')
        top_combination = top_combination.to_dict()

        return Response({
            'performance_data': performance_data,
            'top_combination': top_combination
        })


class FilteredAggregationView(APIView):
    def get(self, request):
        df = load_data()
        aggregated_data = filtered_aggregation(df)
        aggregated_data = aggregated_data.to_dict(orient='records')

        return Response({
            'aggregated_data': aggregated_data
        })
