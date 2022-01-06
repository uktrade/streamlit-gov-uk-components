#!/bin/bash

# Not completely sure, but I think the below are needed because of
# https://github.com/facebook/create-react-app/issues/10356

sed -i '' -e 's|import { Table, Vector } from "apache-arrow";|import { Vector } from "apache-arrow/vector";import { Table } from "apache-arrow/table";|g' ./node_modules/streamlit-component-lib/dist/ArrowTable.d.ts
sed -i '' -e 's|import { Table, Type } from "apache-arrow";||g' ./node_modules/streamlit-component-lib/dist/ArrowTable.js

mv ./node_modules/apache-arrow/ipc/reader.mjs ./node_modules/apache-arrow/ipc/reader.js
mv ./node_modules/apache-arrow/util/buffer.mjs ./node_modules/apache-arrow/util/buffer.js
mv ./node_modules/apache-arrow/io/adapters.mjs ./node_modules/apache-arrow/io/adapters.js
mv ./node_modules/apache-arrow/builder.mjs ./node_modules/apache-arrow/builder.js
mv ./node_modules/apache-arrow/ipc/writer.mjs ./node_modules/apache-arrow/ipc/writer.js
mv ./node_modules/apache-arrow/table.mjs ./node_modules/apache-arrow/table.js
mv ./node_modules/apache-arrow/io/stream.mjs ./node_modules/apache-arrow/io/stream.js
mv ./node_modules/apache-arrow/vector/index.mjs ./node_modules/apache-arrow/vector/index.js
mv ./node_modules/apache-arrow/io/whatwg/iterable.mjs ./node_modules/apache-arrow/io/whatwg/iterable.js
mv ./node_modules/apache-arrow/io/whatwg/reader.mjs ./node_modules/apache-arrow/io/whatwg/reader.js
mv ./node_modules/apache-arrow/io/whatwg/writer.mjs ./node_modules/apache-arrow/io/whatwg/writer.js
mv ./node_modules/apache-arrow/ipc/message.mjs ./node_modules/apache-arrow/ipc/message.js
mv ./node_modules/apache-arrow/io/interfaces.mjs ./node_modules/apache-arrow/io/interfaces.js
mv ./node_modules/apache-arrow/io/file.mjs ./node_modules/apache-arrow/io/file.js
mv ./node_modules/apache-arrow/io/whatwg/builder.mjs ./node_modules/apache-arrow/io/whatwg/builder.js
