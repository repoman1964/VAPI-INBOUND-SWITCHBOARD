from django.urls import path



from .views import (
    testAndDirectInboundCall,   
    )

app_name = 'inbound'  # Declaring the namespace for this URLs module

urlpatterns = [ 



    path('controller/', testAndDirectInboundCall, name='inbound_controller'),

    # path('/', inboundPageView.as_view(), name='inbound'),

    # path('inbound/shuttle-service/', demoBotShuttleService.as_view(), name='demo_bot_shuttle'),
    # path('inbound/restaurant/', demoBotRestaurant.as_view(), name='demo_bot_restaurant'),
    # path('inbound/med-spa/', demoBotMedSpa.as_view(), name='demo_bot_medspa'),

    
    # path('outbound/', outboundPageView.as_view(), name='outbound'),

    # path('outbound/lead-gen/', demoBotLeadGen.as_view(), name='demo_lead_gen'),
    # path('outbound/db-reactivation/', demoBotDBReactivation.as_view(), name='demo_db_reactivation'),
    # path('outbound/review-management/', demoBotReviewManagement.as_view(), name='demo_review_management'),

   

    # path('conversational-ai-assistants/', conversationalAssistantsPageView.as_view(), name='conversational_ai'),
    #  path('why-us/', whyUsPageView.as_view(), name='whyus'),
    #   path('ai-automations/', aiAutomationsPageView.as_view(), name='ai_automations'),


    # path('test/', views.getTestView, name='get_test'),
    # path('why-us/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('pricing/', views.pricing, name='pricing'),
    # path('faq/', views.faq, name='faq'),
    # path('blog_post/', views.blog_post, name='blog_post'),
    # path('blog_home/', views.blog_home, name='blog_home'), 
    # path('portfolio_overview/', views.portfolio_overview, name='portfolio_overview'),
    # path('portfolio_item/', views.portfolio_item, name='portfolio_item'),        
]

