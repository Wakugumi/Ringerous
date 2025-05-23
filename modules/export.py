import csv

def export_results_txt(results, filepath):
    with open(filepath, 'w') as f:
        for prop, res in results.items():
            f.write(f"{prop}: {'✔️' if res['result'] else '❌'}\n")
            if not res["result"] and res["counterexample"] is not None:
                f.write(f"  Counterexample: {res['counterexample']}\n")
            f.write("\n")

def export_results_csv(results, filepath):
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Property", "Result", "Counterexample"])
        for prop, res in results.items():
            writer.writerow([
                prop,
                "True" if res['result'] else "False",
                "" if res["result"] else str(res["counterexample"])
            ])

def export_batch_results_csv(batch_results, filepath):
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        headers = ["Filename", "Property", "Result", "Counterexample"]
        writer.writerow(headers)
        for filename, result_dict in batch_results.items():
            for prop, res in result_dict.items():
                writer.writerow([
                    filename,
                    prop,
                    "True" if res["result"] else "False",
                    "" if res["result"] else str(res["counterexample"])
                ])
