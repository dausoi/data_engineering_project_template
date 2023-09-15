"""
create some schema
"""

from yoyo import step

__depends__ = {'20221023_01_JVZ9p-create-bitcoin-schema'}

steps = [
  step(
      "CREATE TABLE foo (id INT, bar VARCHAR(20), PRIMARY KEY (id))",
      "DROP TABLE foo",
  ),
  step(
      "ALTER TABLE foo ADD COLUMN baz INT NOT NULL"
  )
]
