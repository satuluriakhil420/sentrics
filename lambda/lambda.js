exports.handler = async function(event, context) {
  console.log("Lambda function executed successfully!");
  return {
    statusCode: 200,
    body: "Hello from Lambda!"
  };
};
