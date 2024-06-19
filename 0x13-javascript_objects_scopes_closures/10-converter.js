#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    return (number >>> 0).toString(base);
  };
};
