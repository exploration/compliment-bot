#!/usr/bin/env ruby

require 'optparse'

options = {}

parser = OptionParser.new do |opts|
  opts.banner = "Usage: generate_activity.rb [options]"
  opts.on("-l PATH_TO_REPO", "--db-location PATH_TO_REPO", "Specify location of activities database") do |path_to_repo|
    options[:db_location] = path_to_repo
  end
end

parser.parse!

# param check
unless options[:db_location]
  puts parser
  exit
end

def get_file_as_string(filename)
  data = []
  f = File.open(filename, "r") 
  f.each_line do |line|
    data << line
  end
  return data
end

data = get_file_as_string "#{options[:db_location]}/activities.txt"
output = []
3.times do
  random = rand(data.length)
  output << data[random]
end

puts output.join.gsub("\n"," ").strip()
