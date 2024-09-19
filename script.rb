require 'faraday'
require 'faraday/retry'

connection = Faraday.new(url: 'https://api.example.com') do |conn|
  conn.request :retry, max: 3, interval: 0.05, backoff_factor: 2
  # Add other middleware or settings here
end

