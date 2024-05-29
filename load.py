#!/usr/bin/pythyon3

from absl import flags, app
from rdflib_neo4j import Neo4jStoreConfig, Neo4jStore, HANDLE_VOCAB_URI_STRATEGY
from rdflib import Graph

FLAGS = flags.FLAGS

def add_options():
  flags.DEFINE_string('host', default = 'bolt://localhost:7687', help = 'host address')
  flags.DEFINE_string('db', default = 'neo4j', help = 'database name')
  flags.DEFINE_string('user', default = 'neo4j', help = 'user name')
  flags.DEFINE_string('password', default = None, help = 'password')
  flags.DEFINE_string('input_rdf', default = None, help = 'path to input rdf')

def main(unused_argv):
  auth_data = {'uri': FLAGS.host,
               'database': FLAGS.db,
               'user': FLAGS.user,
               'pwd': FLAGS.password}

  # Define your custom mappings & store config
  config = Neo4jStoreConfig(auth_data=auth_data,
                            handle_vocab_uri_strategy=HANDLE_VOCAB_URI_STRATEGY.IGNORE,
                            batching=True)

  # Create the RDF Graph, parse & ingest the data to Neo4j, and close the store(If the field batching is set to True in the Neo4jStoreConfig, remember to close the store to prevent the loss of any uncommitted records.)
  neo4j_aura = Graph(store=Neo4jStore(config=config))
  # Calling the parse method will implictly open the store
  neo4j_aura.parse(FLAGS.input_rdf, format="ttl")
  neo4j_aura.close(True)

if __name__ == "__main__":
  add_options()
  app.run(main)

