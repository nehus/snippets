# from django.shortcuts import render
# # from snippets.models import *
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
from rest_framework.response import Response
import json
import pika
import sys
import urllib2
import config as cfg
from ast import *



# import config as cfg




# @csrf_exempt
# def index(request):
# 	"""
# 	List all code snippets, or create a new snippet.
# 	"""
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return Response(serializer.data)

# 	if request.method == 'POST':
# 		serializer = SnippetSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()

# 			content = JSONRenderer().render(serializer.data)
# 			message = json.dumps(content)	

# 			connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# 			channel = connection.channel()

# 			# Declare queue to send data
# 			channel.queue_declare(queue='mytopic')

			
			

# 			# Send data
# 			channel.basic_publish(exchange='', routing_key='mytopic', body=message)
# 			print(" [x] Sent data to RabbitMQ")
# 			connection.close()
			
# 			return Response(serializer.data, status=201)
		
# 		return Response(serializer.errors, status=400)





# # def index(request):

# # 	if request.method == "POST":
# # 		print "hello"		
# # 		name = request.POST.get('name')
# # 		print name
# # 		d = request.POST.get('discription')
# # 		print d

# # 	return render (request,"snippets/index.html")



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def index(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        # Connect to RabbitMQ and create channel
        return Response(serializer.data)  

    if request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = JSONRenderer().render(serializer.data)
            message = json.dumps(content)
            # response = urllib2.urlopen('http://localhost:15672/').read()
            # response = literal_eval(response)
            # host = str(response['localhost'])
            # vhost = str(response['localhost'])
            # credentials = pika.PlainCredentials(Response['admin'],Response['admin'])

            







            

            connection = pika.BlockingConnection(pika.ConnectionParameters(host=cfg.RABBIT_HOST))
            print  connection
            channel = connection.channel()
            channel.queue_declare(queue=cfg.QUEUE_TOPIC)


# Declare queue to send data
            # channel.queue_declare(queue='myqueue')
                 
# Send data
            channel.basic_publish(exchange='',
                      routing_key=cfg.QUEUE_TOPIC,
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))           

            print(" [x] Sent %r" % message)
            print(" [x] Sent data to RabbitMQ")
            connection.close()












            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
# Create your views here.










# message = ' '.join(sys.argv[1:]) or "info: Hello World!"








    
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)

#         connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#         channel = connection.channel()


# # # # # Declare and listen queue
#         channel.queue_declare(queue='mytopic')#here we are creating the veiw
#         print(' [*] Waiting for messages. To exit press CTRL+C')

# # # # # Function process and print data
#         def callback(ch, method, properties, body):
#             print("Method: {}".format(method))
#             print("Properties: {}".format(properties))
#             print body

#             data = json.loads(body)
#             print("ID: {}".format(data['id']))
#             print("Name: {}".format(data['name']))
#             print('Description: {}'.format(data['description']))

# # # Listen and receive data from queue
#             channel.basic_consume(callback, queue='mytopic',no_ack=True)
#             channel.start_consuming()


               




        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 