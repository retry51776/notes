# Ruby

## Packages
- sidekiq `uses by Gitlab acts as task queue; uses redis`
```ruby
require 'sidekiq'

Sidekiq.configure_client do |config|
    config.reids = { db: 1}
end

class XYZ
    include Sidekiq::Worker

    def perform(task)
        case task
        when "xyz"
            puts "done xyz"
        when "sleep"
            sleep 10
            put "done sleep"
        end
    end
end
```