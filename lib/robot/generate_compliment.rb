#!/usr/bin/env ruby

require 'optparse'

options = {}

parser = OptionParser.new do |opts|
  opts.banner = "Usage: generate_compliment.rb [options]"
  opts.on("-l PATH_TO_REPO", "--db-location PATH_TO_REPO", "Specify location of compliments database files") do |path_to_repo|
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

adverbs = get_file_as_string "#{options[:db_location]}/adverbs.txt"
adjectives = get_file_as_string "#{options[:db_location]}/adjectives.txt"

output = []

output << adverbs[rand(adverbs.length)]
output << adjectives[rand(adjectives.length)]

output_text = output.join.gsub("\n",' ').strip()
puts "you are #{output_text}"
