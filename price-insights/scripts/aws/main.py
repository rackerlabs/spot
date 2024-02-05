import boto3
import json
from datetime import datetime

def fetch_spot_prices(instance_types, regions, profile_name='spot-pricing'):
    results = []

    for region in regions:
        session = boto3.Session(profile_name=profile_name, region_name=region)
        ec2_client = session.client('ec2')

        response = ec2_client.describe_spot_price_history(
            InstanceTypes=instance_types,
            ProductDescriptions=["Linux/UNIX"],
        )

        for entry in response['SpotPriceHistory']:
            result = {
                'InstanceType': entry['InstanceType'],
                'Region': region,
                'AvailabilityZone': entry['AvailabilityZone'],
                'SpotPrice': entry['SpotPrice'],
                'Timestamp': entry['Timestamp'].isoformat(),
            }
            results.append(result)

    return results

def write_to_json(data, output_file='spot_prices.json'):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    instance_types = ['t2.micro', 't2.medium', 'm6g.xlarge', 'm6g.2xlarge', 'm6g.4xlarge', 'c4.large', 'c4.xlarge', 'c4.2xlarge', 'c4.4xlarge', 'r4.large', 'r4.xlarge', 'r4.2xlarge', 'r4.4xlarge']
    regions = ['us-east-1', 'us-east-2']

    spot_prices = fetch_spot_prices(instance_types, regions)
    write_to_json(spot_prices)

    print("Spot prices fetched and written to spot_prices.json.")
