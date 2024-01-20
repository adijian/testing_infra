import ast
import csv

if __name__ == "__main__":
    data = {
        "{'name': 'TestBundleCollection_test_collection', 'error': 'Pass', 'elapsed_time': 0.73, 'start_time': '2024-01-20 21:07:08'}": [
            {
                "{'name': 'TestBundle_test_bundle', 'error': 'Pass', 'elapsed_time': 0.25, 'start_time': '2024-01-20 21:07:10'}": [
                    {
                        "{'name': 'TestOne_test', 'error': 'Pass', 'elapsed_time': 0.08, 'start_time': '2024-01-20 21:07:12'}": [
                            "{'name': 'ActionOne_action', 'error': 'Pass', 'elapsed_time': 0.05, 'start_time': '2024-01-20 21:07:14'}",
                            "{'name': 'ActionOne_action', 'error': 'Pass', 'elapsed_time': 0.05, 'start_time': '2024-01-20 21:07:14'}"
                        ]
                    },
                    {
                        "{'name': 'TestOne_test', 'error': 'Pass', 'elapsed_time': 0.1, 'start_time': '2024-01-20 21:07:19'}": [
                            "{'name': 'ActionOne_action', 'error': 'Pass', 'elapsed_time': 0.05, 'start_time': '2024-01-20 21:07:22'}",
                            "{'name': 'ActionOne_action', 'error': 'Pass', 'elapsed_time': 0.05, 'start_time': '2024-01-20 21:07:22'}"
                        ]
                    }
                ]
            },
            {
                "{'name': 'TestBundle_test_bundle', 'error': 'Pass', 'elapsed_time': 0.42, 'start_time': '2024-01-20 21:07:27'}": [
                    {
                        "{'name': 'TestOne_test', 'error': 'Pass', 'elapsed_time': 0.08, 'start_time': '2024-01-20 21:07:29'}": [
                            "{'name': 'ActionOne_action', 'error': 'Pass', 'elapsed_time': 0.05, 'start_time': '2024-01-20 21:07:31'}",
                            "{'name': 'ActionOne_action', 'error': 'Pass', 'elapsed_time': 0.05, 'start_time': '2024-01-20 21:07:31'}"
                        ]
                    },
                    {
                        "{'name': 'TestOne_test', 'error': 'Pass', 'elapsed_time': 0.08, 'start_time': '2024-01-20 21:07:36'}": [
                            "{'name': 'ActionOne_action', 'error': 'Pass', 'elapsed_time': 0.05, 'start_time': '2024-01-20 21:07:38'}",
                            "{'name': 'ActionOne_action', 'error': 'Pass', 'elapsed_time': 0.05, 'start_time': '2024-01-20 21:07:38'}"
                        ]
                    }
                ]
            }
        ]
    }
    headers = []
    flat_data = []
    for bundle_collection in data:
        if not headers:
            headers.append(list(ast.literal_eval(bundle_collection).keys()))
        flat_data.append(list(ast.literal_eval(bundle_collection).values()))
        dict_bundle_collection = data[bundle_collection]
        for test_bundle in dict_bundle_collection:
            flat_data.append(list(ast.literal_eval(list(test_bundle.keys())[0]).values()))
            for test in test_bundle:
                flat_data.append(list(ast.literal_eval(test).values()))

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # writer.writerows(headers)
        print(headers)
        writer.writerows(headers)
        writer.writerows(flat_data)

        # for data_piece in flat_data:
        #     writer.writerows(f'{data_piece}')
