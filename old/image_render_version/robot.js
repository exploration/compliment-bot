// we use this to get the args
system = require('system');

// check passed text
if (system.args.length === 1 || system.args.length === 2) {
    console.log('Usage: robot.js output_file.png "text to render"');
    phantom.exit();
}

// you only pass one parameter: the text you want to render
var outputFile = system.args[1]
var renderThis = system.args[2];
var page = require('webpage').create();

page.open("file:///home/pi/git/activity-robot/lib/html/activity-robot/public/index.html?q=" + renderThis, function() {
  page.render(outputFile);
  phantom.exit();
});
