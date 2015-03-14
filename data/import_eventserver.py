"""
Import sample data for classification engine
"""

import predictionio
import argparse
import csv

def import_events(client, file):
  with open("train.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    d = list(reader)
    prev_sent_id = 0
    d = d[1:]
    for line in d:
      if prev_sent_id == line[1]:        
        continue
      prev_sent_id = line[1]
      client.create_event(
        event="$set",
        entity_type="user",
        entity_id=int(line[0]),
        properties= {
          "description" : line[2],
          "id" : int(line[1]),
          "sentiment_id": int(line[3])
        }
      )
  f.close()                                                                                                                                           

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import sample data for classification engine")
  parser.add_argument('--access_key', default='invald_access_key')
  parser.add_argument('--url', default="http://localhost:7070")
  parser.add_argument('--file', default="./train.tsv")

  args = parser.parse_args()
  print args

  client = predictionio.EventClient(
    access_key='VgN3DsprZExK4etsYORKeX6madpwYkcRWSUkUkTfygWdftwfD9YMf4ytyoJcELTW'                                                                                                   ,
    url=args.url,
    threads=5,
    qsize=500)
  import_events(client, args.file)
