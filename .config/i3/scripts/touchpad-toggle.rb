#!/usr/bin/ruby

def notify(msg)
	`notify-send -t 1500 -i emblem-important-symbolic "#{msg}"`
end


puts "Toggling touchpad on/off"

x = `xinput list | grep -i touchpad`
if x =~ /id=(\d+)/i
	id = $~[1]
	puts "touchpad found at deveice id #{id}"

	x = `xinput list-props #{id} | grep -i 'device enabled'`
	if x =~ /(\d)$/
		state = $~[1]
		if state == "1"
			puts "disabling Touchpad"
			`xinput disable #{id}`
			notify("Touch Disabled")
		else
			puts "enabling Touchpad"
			`xinput enable #{id}`
			notify("Touchbad Enabled")
		end
	else
		puts "Can't detect touchpad state"
	end
else
	puts "No touchpad found"
end
