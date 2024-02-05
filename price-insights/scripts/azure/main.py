#!/usr/bin/env python3
import requests
import json

def main():
    api_url = "https://prices.azure.com/api/retail/prices?api-version=2021-10-01-preview"
    azure_sku_names = [
        'Standard_A1_v2', 'Standard_F2s', 'Standard_D4ps_v5', 'Standard_D8ps_v5', 'Standard_D16ps_v5',
        'Standard_F2', 'Standard_F4', 'Standard_F8', 'Standard_F16',
        'Standard_E2s_v5', 'Standard_E4s_v5', 'Standard_E8s_v5', 'Standard_E16s_v5'
    ]

    sku_filters = " or ".join([f"armSkuName eq '{sku}'" for sku in azure_sku_names])
    query = f"(armRegionName eq 'southcentralus' or armRegionName eq 'eastus') and serviceName eq 'Virtual Machines' and priceType eq 'Consumption' and contains(meterName, 'Spot') and ({sku_filters})"

    response = requests.get(api_url, params={'$filter': query})
    json_data = json.loads(response.text)

    data_southcentralus = []
    data_eastus = []

    # Filter out entries where productName contains "Windows" and split by region
    for item in json_data['Items']:
        if 'Windows' not in item.get('productName', ''):
            if item['armRegionName'] == 'southcentralus':
                data_southcentralus.append(item)
            elif item['armRegionName'] == 'eastus':
                data_eastus.append(item)

    def print_data(region_name, data):
        print(f"Region: {region_name}")
        print(f"{'SKU Name':<20} {'Retail Price':<15}")
        for item in data:
            print(f"{item['armSkuName']:<20} {item['retailPrice']:<15}")
        print("\n")

    print_data('South Central US', data_southcentralus)
    print_data('East US', data_eastus)

if __name__ == "__main__":
    main()
