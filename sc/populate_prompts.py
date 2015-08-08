import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sc.settings")

from se.models import Pillar, Prompt
import datetime

def create_pillars():
    pillars = [
        "Living Consciously",
        "Self-Acceptance",
        "Self-Responsibility",
        "Self-Assertiveness",
        "Living Purposefully",
        "Personal Integrity",
        "31 Week Program",
    ]

    for pillar in pillars:
        p = Pillar.objects.create(content = pillar)
        p.save()
        print(str(p.id) + ": " + p.content)

def create_prompts():
    prompts = [
        #{ 'pillar':  , 'week':  , 'content': '', },
        { 'pillar': 1, 'week': 1, 'content': 'Living consciously to me means', },
        { 'pillar': 1, 'week': 1, 'content': 'If I bring 5 percent more awareness to my activities today,', },
        { 'pillar': 1, 'week': 1, 'content': 'If I pay more attention to how I deal with people today,', },
        { 'pillar': 1, 'week': 1, 'content': 'If I bring 5 percent more awareness to my most important relationships,', },
        { 'pillar': 1, 'week': 1, 'content': 'When I reflect on how I would feel if I lived more consciously, ', },
        { 'pillar': 1, 'week': 1, 'content': 'When I reflect on what happens when I bring 5 percent more awareness to my activities, ', },
        { 'pillar': 1, 'week': 1, 'content': 'When I reflect on what happens when I pay more attention to how I deal with people, ', },
        { 'pillar': 1, 'week': 1, 'content': 'When I reflect on what happens when I bring 5 percent more awareness to my most important relationships, ', },
        { 'pillar': 1, 'week': 2, 'content': 'If I bring 5 percent more awareness to when I am mentally active and when I am mentally passive, I might see that ', },
        { 'pillar': 1, 'week': 2, 'content': 'If I bring 5 percent more awareness to my relationship with my employees, ', },
        { 'pillar': 1, 'week': 2, 'content': 'If I bring 5 percent more awareness to my insecurities, ', },
        { 'pillar': 1, 'week': 2, 'content': 'If I bring 5 percent more awareness to my depression, ', },
        { 'pillar': 1, 'week': 3, 'content': 'If I bring 5 percent more awareness to my anxiety, ', },
        { 'pillar': 1, 'week': 3, 'content': 'If I bring 5 percent more awareness to my concern about my security, ', },
        { 'pillar': 1, 'week': 3, 'content': 'If I bring 5 percent more awareness to my security, ', },
        { 'pillar': 1, 'week': 3, 'content': 'If I bring 5 percent more awareness to my impulses to avoid unpleasant facts, ', },
        { 'pillar': 1, 'week': 4, 'content': 'If I bring 5 percent more awareness to my needs and wants, ', },
        { 'pillar': 1, 'week': 4, 'content': 'If I bring 5 percent more awareness to my deepest values and goals, ', },
        { 'pillar': 1, 'week': 4, 'content': 'If I bring 5 percent more awareness to my emotions, ', },
        { 'pillar': 1, 'week': 4, 'content': 'If I bring 5 percent more awareness to my priorities, ', },
        { 'pillar': 1, 'week': 5, 'content': 'If I bring 5 percent more awareness to how I sometimes stand in my own way, ', },
        { 'pillar': 1, 'week': 5, 'content': 'If I bring 5 percent more awareness to the outcomes of my actions, ', },
        { 'pillar': 1, 'week': 5, 'content': 'If I bring 5 percent more awareness to how I sometimes make it difficult for people to give me what I want, ', },
        { 'pillar': 1, 'week': 5, 'content': 'If I bring 5 percent more awareness to what my job requires of me, ', },
        { 'pillar': 1, 'week': 6, 'content': 'If I bring 5 percent more awareness to what I know about being an effective manager, ', },
        { 'pillar': 1, 'week': 6, 'content': 'If I bring 5 percent more awareness to what I know about building consensus, ', },
        { 'pillar': 1, 'week': 6, 'content': 'If I bring 5 percent more awareness to what I know about appropriate delegating, ', },
        { 'pillar': 1, 'week': 6, 'content': 'If I bring 5 percent more awareness to my fear of operating more consciously, ', },
        { 'pillar': 1, 'week': 2, 'content': 'If I imagine bringing more consciousness into my life, ', },
        { 'pillar': 1, 'week': 2, 'content': 'The scary thing about being more conscious might be ', },
        { 'pillar': 1, 'week': 7, 'content': 'The hard thing about staying fully conscious is ', },
        { 'pillar': 1, 'week': 7, 'content': 'The good thing about being fully conscious is ', },
        { 'pillar': 1, 'week': 7, 'content': 'If I were to stay more conscious, ', },
        { 'pillar': 1, 'week': 7, 'content': 'If I were to experiment with raising my consciousness 5 percent about ', },
        { 'pillar': 2, 'week': 1, 'content': 'Self-acceptance to me means ', },
        { 'pillar': 2, 'week': 1, 'content': 'If I am more accepting of my body, ', },
        { 'pillar': 2, 'week': 1, 'content': 'When I deny and disown my body, ', },
        { 'pillar': 2, 'week': 1, 'content': 'If I am more accepting of my conflicts, ', },
        { 'pillar': 2, 'week': 1, 'content': 'When I deny and disown my conflicts, ', },
        { 'pillar': 2, 'week': 2, 'content': 'If I am more accepting of my feelings, ', },
        { 'pillar': 2, 'week': 2, 'content': 'When I deny and disown my feelings, ', },
        { 'pillar': 2, 'week': 2, 'content': 'If I am more accepting of my thoughts, ', },
        { 'pillar': 2, 'week': 2, 'content': 'When I deny and disown my thoughts, ', },
        { 'pillar': 2, 'week': 3, 'content': 'If I am more accepting of my actions, ', },
        { 'pillar': 2, 'week': 3, 'content': 'When I deny and disown my actions, ', },
        { 'pillar': 2, 'week': 3, 'content': 'I am becoming aware ', },
        { 'pillar': 2, 'week': 3, 'content': 'If I am willing to be realistic about my assets and shortcomings, ', },
        { 'pillar': 2, 'week': 4, 'content': 'If I am more accepting of my fears, ', },
        { 'pillar': 2, 'week': 4, 'content': 'When I deny and disown my fears, ', },
        { 'pillar': 2, 'week': 4, 'content': 'If I am more accepting of my anger, ', },
        { 'pillar': 2, 'week': 4, 'content': 'When I deny and disown my anger, ', },
        { 'pillar': 2, 'week': 2, 'content': 'If I am more accepting of my sexuality, ', },
        { 'pillar': 2, 'week': 2, 'content': 'When I deny and disown my sexuality, ', },
        { 'pillar': 2, 'week': 5, 'content': 'If I am more accepting of my excitement, ', },
        { 'pillar': 2, 'week': 5, 'content': 'When I deny and disown my excitement, ', },
        { 'pillar': 2, 'week': 5, 'content': 'If I am more accepting of my joy, ', },
        { 'pillar': 2, 'week': 5, 'content': 'When I deny and disown my joy, ', },
        { 'pillar': 2, 'week': 6, 'content': 'If I am willing to see what I see and know what I know, ', },
        { 'pillar': 2, 'week': 6, 'content': 'If I bring a high level of consciousness to my fears, ', },
        { 'pillar': 2, 'week': 6, 'content': 'If I bring a high level of consciousness to my pain, ', },
        { 'pillar': 2, 'week': 6, 'content': 'If I bring a high level of consciousness to my sexuality, ', },
        { 'pillar': 2, 'week': 6, 'content': 'If I bring a high level of consciousness to my excitement, ', },
        { 'pillar': 2, 'week': 6, 'content': 'If I bring a high level of consciousness to my joy, ', },
        { 'pillar': 2, 'week': 7, 'content': 'When I think of the consequences of not accepting myself, ', },
        { 'pillar': 2, 'week': 7, 'content': 'If I accept the fact that what is, is, regardless of whether I admit it, ', },
        { 'pillar': 2, 'week': 7, 'content': 'I am beginning to see that ', },
        { 'pillar': 3, 'week': 1, 'content': 'Self-responsibility to me means ', },
        { 'pillar': 3, 'week': 1, 'content': 'At the thought of being responsible for my own existence, ', },
        { 'pillar': 3, 'week': 1, 'content': 'If I accepted responsibility for my own existence, that would mean ', },
        { 'pillar': 3, 'week': 1, 'content': 'When I avoid responsibility for my own existence, ', },
        { 'pillar': 3, 'week': 2, 'content': 'If I accept 5 percent more responsibility for the attainment of my own goals, ', },
        { 'pillar': 3, 'week': 2, 'content': 'When I avoid responsibility for the attainment of my goals, ', },
        { 'pillar': 3, 'week': 2, 'content': 'If I took more responsibility for the success of my relationships, ', },
        { 'pillar': 3, 'week': 2, 'content': 'Sometimes I keep myself passive by ', },
        { 'pillar': 3, 'week': 3, 'content': 'If I take responsibility for what I do about the messages I received from my mother, ', },
        { 'pillar': 3, 'week': 3, 'content': 'If I take responsibility for what I do about the messages I received from my father, ', },
        { 'pillar': 3, 'week': 3, 'content': 'If I take responsibility for the ideas I accept or reject, ', },
        { 'pillar': 3, 'week': 3, 'content': 'If I bring greater awareness to the ideas that motivate me, ', },
        { 'pillar': 3, 'week': 4, 'content': 'If I accept 5 percent more responsibilty for my personal happiness, ', },
        { 'pillar': 3, 'week': 4, 'content': 'If I avoid responsibility for my personal happiness, ', },
        { 'pillar': 3, 'week': 4, 'content': 'If I accept 5 percent more responsibility for my choice of companions, ', },
        { 'pillar': 3, 'week': 4, 'content': 'When I avoid responsibility for my choice of companions, ', },
        { 'pillar': 3, 'week': 5, 'content': 'If I accept 5 percent more responsibility for the words that come out of my mouth, ', },
        { 'pillar': 3, 'week': 5, 'content': 'When I avoid responsibilty for the words that come out of my mouth, ', },
        { 'pillar': 3, 'week': 5, 'content': 'If I bring greater awareness to the things I tell myself, ', },
        { 'pillar': 3, 'week': 5, 'content': 'If I take responsibility for the things I tell myself, ', },
        { 'pillar': 3, 'week': 6, 'content': 'I make myself feel helpless when I ', },
        { 'pillar': 3, 'week': 6, 'content': 'I make myself feel depress when I ', },
        { 'pillar': 3, 'week': 6, 'content': 'I make myself anxious when I ', },
        { 'pillar': 3, 'week': 6, 'content': 'If I take responsibilty for making myself helpless, ', },
        { 'pillar': 3, 'week': 6, 'content': 'If I take responsibilty for making myself depressed, ', },
        { 'pillar': 3, 'week': 6, 'content': 'If I take responsibilty for making myself anxious, ', },
        { 'pillar': 3, 'week': 7, 'content': 'When I am ready to understand what I have been writing, ', },
        { 'pillar': 3, 'week': 7, 'content': 'It is not easy for me to admit that ', },
        { 'pillar': 3, 'week': 7, 'content': 'If I take responsibility for my present standard of living, ', },
        { 'pillar': 3, 'week': 8, 'content': 'I feel most self-responsible when I ', },
        { 'pillar': 3, 'week': 8, 'content': 'I feel least self-responsible when I ', },
        { 'pillar': 3, 'week': 8, 'content': 'If I am not here on earth to live up to anyone\'s expectations, ', },
        { 'pillar': 3, 'week': 8, 'content': 'If my life belongs to me, ', },
        { 'pillar': 3, 'week': 9, 'content': 'If I give up the lie of being unable to change, ', },
        { 'pillar': 3, 'week': 9, 'content': 'If I take responsibility for what I make of my life from this point on, ', },
        { 'pillar': 3, 'week': 9, 'content': 'If no one is coming to rescue me, ', },
        { 'pillar': 3, 'week': 9, 'content': 'I am becoming aware ', },
        { 'pillar': 4, 'week': 1, 'content': 'Self-assertiveness to me means ', },
        { 'pillar': 4, 'week': 1, 'content': 'If I lived 5 percent more self-assertively today, ', },
        { 'pillar': 4, 'week': 1, 'content': 'If someone had told me my wants were important, ', },
        { 'pillar': 4, 'week': 1, 'content': 'If I had the courage to treat my wants as important, ', },
        { 'pillar': 4, 'week': 2, 'content': 'If I brought more awareness to my deepest needs and wants, ', },
        { 'pillar': 4, 'week': 2, 'content': 'When I ignore my deepest yearnings, ', },
        { 'pillar': 4, 'week': 2, 'content': 'If I were willing to say yes when I want to say yes and no when I want to say no, ', },
        { 'pillar': 4, 'week': 2, 'content': 'If I were willing to voice my thoughts and opinions more often, ', },
        { 'pillar': 4, 'week': 3, 'content': 'When I suppress my thoughts and opinions, ', },
        { 'pillar': 4, 'week': 3, 'content': 'If I am willing to ask for what I want, ', },
        { 'pillar': 4, 'week': 3, 'content': 'When I remain silent about what I want, ', },
        { 'pillar': 4, 'week': 4, 'content': 'If I am willing to let people hear the music inside me, ', },
        { 'pillar': 4, 'week': 4, 'content': 'If I am willing to let myself hear the music inside me, ', },
        { 'pillar': 4, 'week': 4, 'content': 'If I am to express 5 percent more of myself today, ', },
        { 'pillar': 4, 'week': 4, 'content': 'When I hide who I really am, ', },
        { 'pillar': 4, 'week': 4, 'content': 'If I want to live more completely, ', },
        { 'pillar': 5, 'week': 1, 'content': 'Living purposefully to me means ', },
        { 'pillar': 5, 'week': 1, 'content': 'If I bring 5 percent more purposefulness to my life today, ', },
        { 'pillar': 5, 'week': 1, 'content': 'If I operate with 5 percent more purposefulness at work, ', },
        { 'pillar': 5, 'week': 2, 'content': 'If I am 5 percent more purposeful in my communications, ', },
        { 'pillar': 5, 'week': 2, 'content': 'If I bring 5 percent more purposefulness to my relationships at work, ', },
        { 'pillar': 5, 'week': 2, 'content': 'If I operate 5 percent more purposefully in my intimate relationships, ', },
        { 'pillar': 5, 'week': 3, 'content': 'If I operate 5 percent more purposefully with my family, ', },
        { 'pillar': 5, 'week': 3, 'content': 'If I operate 5 percent more purposefully with my friends, ', },
        { 'pillar': 5, 'week': 4, 'content': 'If I am 5 percent more purposeful about my deepest yearnings, ', },
        { 'pillar': 5, 'week': 4, 'content': 'If I am 5 percent more purposeful about taking care of my needs, ', },
        { 'pillar': 5, 'week': 4, 'content': 'If I took more responsibility for fulfulling my wants, ', },
        { 'pillar': 6, 'week': 1, 'content': 'If I bring 5 percent more integrity into my life, ', },
        { 'pillar': 6, 'week': 1, 'content': 'At the thought of going against my parents\' values, ', },
        { 'pillar': 6, 'week': 1, 'content': 'If I were to think for myself about the values I want to live by, ', },
        { 'pillar': 6, 'week': 1, 'content': 'Integrity to me means ', },
        { 'pillar': 6, 'week': 2, 'content': 'If I think about the areas where I find it difficult to practice full integrity, ', },
        { 'pillar': 6, 'week': 2, 'content': 'If I bring a higher level of consciousness to the areas where I find it difficult to practice full integrity, ', },
        { 'pillar': 6, 'week': 2, 'content': 'If I bring 5 percent more integrity into my life, ', },
        { 'pillar': 6, 'week': 2, 'content': 'If I bring 5 percent more integrity into my work, ', },
        { 'pillar': 6, 'week': 3, 'content': 'If I bring 5 percent more integrity into my relationships, ', },
        { 'pillar': 6, 'week': 3, 'content': 'If I remain loyal to the values I truly believe are right, ', },
        { 'pillar': 6, 'week': 3, 'content': 'If I refuse to live by values I do not respect, ', },
        { 'pillar': 6, 'week': 3, 'content': 'If I treat my self-esteem as a high priority, ', },
        { 'content': 'When my mother saw me making a mistake, ', },
        { 'content': 'When my father saw me making a mistake, ', },
        { 'content': 'When I catch myself making a mistake, ', },
        { 'content': 'If someone had told me it\'s alright to make mistakes, ', },
        { 'content': 'What I hear myself saying is ', },
        { 'content': 'If I had the courage to allow myself mistakes, ', },
        { 'content': 'If I were more compassionate about my mistakes, ', },
        { 'content': 'As I learn a better attitude toward making mistakes, ', },
        { 'pillar': 7, 'week': 1, 'content': 'If I bring more awareness to my life today, ', },
        { 'pillar': 7, 'week': 1, 'content': 'If I take more responsibility for my choices and actions today, ', },
        { 'pillar': 7, 'week': 1, 'content': 'If I pay more attention to how I deal with people today, ', },
        { 'pillar': 7, 'week': 1, 'content': 'If I boost my energy level by 5 percent today, ', },
        { 'pillar': 7, 'week': 2, 'content': 'If I bring 5 percent more awareness to my most important relationships, ', },
        { 'pillar': 7, 'week': 2, 'content': 'If I bring 5 percent more awareness to my insecurities, ', },
        { 'pillar': 7, 'week': 2, 'content': 'If I bring 5 percent more awareness to my deepest needs and wants, ', },
        { 'pillar': 7, 'week': 2, 'content': 'If I bring 5 percent more awareness to my emotions, ', },
        { 'pillar': 7, 'week': 3, 'content': 'If I treat listening as a creative act, ', },
        { 'pillar': 7, 'week': 3, 'content': 'If I notice how people are affected by the quality of my listening, ', },
        { 'pillar': 7, 'week': 3, 'content': 'If I bring more awareness to my dealings with people today, ', },
        { 'pillar': 7, 'week': 3, 'content': 'If I commit to dealing with people fairly and benevolently, ', },
        { 'pillar': 7, 'week': 4, 'content': 'If I bring a higher level of self-esteem to my activities today, ', },
        { 'pillar': 7, 'week': 4, 'content': 'If I bring a higher level of self-esteem to my dealings with people today, ', },
        { 'pillar': 7, 'week': 4, 'content': 'If I am 5 percent more self accepting today, ', },
        { 'pillar': 7, 'week': 4, 'content': 'If I am self accepting even when I make mistakes, ', },
        { 'pillar': 7, 'week': 4, 'content': 'If I am self accepting even when I feel confused and overwhelmed, ', },
        { 'pillar': 7, 'week': 5, 'content': 'If I am more accepting of my own body, ', },
        { 'pillar': 7, 'week': 5, 'content': 'If I deny and disown my body, ', },
        { 'pillar': 7, 'week': 5, 'content': 'If I deny or disown my conflicts, ', },
        { 'pillar': 7, 'week': 5, 'content': 'If I am more accepting of all the parts of me, ', },
        { 'pillar': 7, 'week': 6, 'content': 'If I wanted to raise my self-esteem today, I could ', },
        { 'pillar': 7, 'week': 6, 'content': 'If I am more acceptin of my feelings, ', },
        { 'pillar': 7, 'week': 6, 'content': 'If I deny and disown my feelings, ', },
        { 'pillar': 7, 'week': 6, 'content': 'If I am more accepting of my thoughts, ', },
        { 'pillar': 7, 'week': 6, 'content': 'If I deny and disown my thoughts, ', },
        { 'pillar': 7, 'week': 7, 'content': 'If I am more accepting of my fears, ', },
        { 'pillar': 7, 'week': 7, 'content': 'If I deny and disown my fears, ', },
        { 'pillar': 7, 'week': 7, 'content': 'If I were more accepting of my pain, ', },
        { 'pillar': 7, 'week': 7, 'content': 'If I deny and disown my pain, ', },
        { 'pillar': 7, 'week': 8, 'content': 'If I am more accepting of my anger, ', },
        { 'pillar': 7, 'week': 8, 'content': 'If I deny and disown my anger, ', },
        { 'pillar': 7, 'week': 8, 'content': 'If I am more accepting of my sexuality, ', },
        { 'pillar': 7, 'week': 8, 'content': 'If I deny and disown my sexuality, ', },
        { 'pillar': 7, 'week': 9, 'content': 'If I am more accepting of my excitement, ', },
        { 'pillar': 7, 'week': 9, 'content': 'If I deny and disown my excitement, ', },
        { 'pillar': 7, 'week': 9, 'content': 'If I am more accepting of my intelligence, ', },
        { 'pillar': 7, 'week': 9, 'content': 'If I deny and disown my intelligence, ', },
        { 'pillar': 7, 'week': 10, 'content': 'If I am more accepting of my joy, ', },
        { 'pillar': 7, 'week': 10, 'content': 'If I deny and disown my joy, ', },
        { 'pillar': 7, 'week': 10, 'content': 'If I bring more awareness to all parts of me, ', },
        { 'pillar': 7, 'week': 10, 'content': 'As I learn to accept all of who I am, ', },
        { 'pillar': 7, 'week': 11, 'content': 'Self-responsibility to me means ', },
        { 'pillar': 7, 'week': 11, 'content': 'If I take 5 percent more responsibility for my life and well-being, ', },
        { 'pillar': 7, 'week': 11, 'content': 'If I avoid responsibility for my life and well-being, ', },
        { 'pillar': 7, 'week': 11, 'content': 'If I take 5 percent more responsibility for the attainment of my goals, ', },
        { 'pillar': 7, 'week': 11, 'content': 'If I avoid responsibility for the attainment of my goals, ', },
        { 'pillar': 7, 'week': 12,'content': 'If I take 5 percent more responsibility for the success of my relationships, ', },
        { 'pillar': 7, 'week': 12, 'content': 'Sometimes I keep myself passive when I ', },
        { 'pillar': 7, 'week': 12, 'content': 'Sometimes I make myself helples when I ', },
        { 'pillar': 7, 'week': 12, 'content': 'I am becoming aware ', },
        { 'pillar': 7, 'week': 13, 'content': 'If I take 5 percent more responsibility for my standard of living, ', },
        { 'pillar': 7, 'week': 13, 'content': 'If I take 5 percent more responsibility for my choice of companions, ', },
        { 'pillar': 7, 'week': 13, 'content': 'If I take 5 percent more responsibility for my personal happiness, ', },
        { 'pillar': 7, 'week': 13, 'content': 'If I take 5 percent more responsibility for the level of my self-esteem, ', },
        { 'pillar': 7, 'week': 14, 'content': 'Self-assertiveness to me means ', },
        { 'pillar': 7, 'week': 14, 'content': 'If I lived 5 percent more assertively today, ', },
        { 'pillar': 7, 'week': 14, 'content': 'If I treated my thoughts and feelings with respect today, ', },
        { 'pillar': 7, 'week': 14, 'content': 'If I treat my wants with respect today, ', },
        { 'pillar': 7, 'week': 15, 'content': 'If, when I was young, someone told me that my thoughts really mattered, ', },
        { 'pillar': 7, 'week': 15, 'content': 'If, when I was young, I had been taught to honor my own life, ', },
        { 'pillar': 7, 'week': 15, 'content': 'If I treat my life as unimportant, ', },
        { 'pillar': 7, 'week': 15, 'content': 'If I were willing to say yes when I mean yes and no when I mean no, ', },
        { 'pillar': 7, 'week': 15, 'content': 'If I were willing to let people hear the music inside of me, ', },
        { 'pillar': 7, 'week': 15, 'content': 'If I were to express 5 percent more of who I am, ', },
        { 'pillar': 7, 'week': 16, 'content': 'Living purposefully to me means ', },
        { 'pillar': 7, 'week': 16, 'content': 'If I bring 5 percent more purposefullness into my life, ', },
        { 'pillar': 7, 'week': 16, 'content': 'If I operate 5 percent more purposefully at work, ', },
        { 'pillar': 7, 'week': 16, 'content': 'If I operate 5 percent more purposefully in my relationships, ', },
        { 'pillar': 7, 'week': 16, 'content': 'If I operate 5 percent more purposefully with my family, ', },
        { 'pillar': 7, 'week': 17, 'content': 'If I were 5 percent more purposeful about my deepest yearnings, ', },
        { 'pillar': 7, 'week': 17, 'content': 'If I take more responsibility for fulfilling my wants, ', },
        { 'pillar': 7, 'week': 17, 'content': 'If I make my happiness a conscious goal, ', },
        { 'pillar': 7, 'week': 18, 'content': 'Integrity to me means ', },
        { 'pillar': 7, 'week': 18, 'content': 'If I look at instances where I find full integrity difficult, ', },
        { 'pillar': 7, 'week': 18, 'content': 'If I bring 5 percent more integrity into my life, ', },
        { 'pillar': 7, 'week': 18, 'content': 'If I bring 5 percent more integrity into my work, ', },
        { 'pillar': 7, 'week': 19, 'content': 'If I bring 5 percent more integrity into my relationships, ', },
        { 'pillar': 7, 'week': 19, 'content': 'If I remain loyal to the values I believe are right, ', },
        { 'pillar': 7, 'week': 19, 'content': 'If I refuse to live by values I do not respect, ', },
        { 'pillar': 7, 'week': 19, 'content': 'If I treat my self respect as high priority, ', },
        { 'pillar': 7, 'week': 20, 'content': 'If the child in me could speak, he would say ', },
        { 'pillar': 7, 'week': 20, 'content': 'If the teenager I once was still exists inside of me, ', },
        { 'pillar': 7, 'week': 20, 'content': 'If my teenage self could speak he would say ', },
        { 'pillar': 7, 'week': 20, 'content': 'At the thought of reaching back to my child-self, ', },
        { 'pillar': 7, 'week': 20, 'content': 'At the thought of reaching back to my teenage-self ', },
        { 'pillar': 7, 'week': 20, 'content': 'If I could make friends with my younger selves, ', },
        { 'pillar': 7, 'week': 21, 'content': 'If my child-self felt accepted by me, ', },
        { 'pillar': 7, 'week': 21, 'content': 'If my teenage-self felt I was on his side, ', },
        { 'pillar': 7, 'week': 21, 'content': 'If my younger selves felt I had compassion for their struggles, ', },
        { 'pillar': 7, 'week': 21, 'content': 'If I could hold my child-self in my arms, ', },
        { 'pillar': 7, 'week': 21, 'content': 'If I could hold my teenage-self in my arms, ', },
        { 'pillar': 7, 'week': 21, 'content': 'If I had the courage and compassion to embrace and love my younger selves, ', },
        { 'pillar': 7, 'week': 22, 'content': 'Sometimes my child-self feels rejected by me when I ', },
        { 'pillar': 7, 'week': 22, 'content': 'Sometimes my teenage-self feels rejected by me when I ', },
        { 'pillar': 7, 'week': 22, 'content': 'One of the things my child-self needs from me and rarely gets is ', },
        { 'pillar': 7, 'week': 22, 'content': 'One of the things my teenage-self needs from me and hasn\'t gotten is ', },
        { 'pillar': 7, 'week': 22, 'content': 'One of the ways my child-self gets back at me for rejecting him is ', },
        { 'pillar': 7, 'week': 22, 'content': 'One of the ways my teenage-self gets back at me for rejecting him is ', },
        { 'pillar': 7, 'week': 23, 'content': 'At the thought of giving my child-self what he needs from me ', },
        { 'pillar': 7, 'week': 23, 'content': 'At the thought of giving my teenage-self what he needs from me ', },
        { 'pillar': 7, 'week': 23, 'content': 'If my child-self and I were to fall in love, ', },
        { 'pillar': 7, 'week': 23, 'content': 'If my teenage-self and I were to fall in love, ', },
        { 'pillar': 7, 'week': 24, 'content': 'If I accept that my child-self may need time to learn to trust me, ', },
        { 'pillar': 7, 'week': 24, 'content': 'If I accept that my teenage-self may need time to learn to trust me, ', },
        { 'pillar': 7, 'week': 24, 'content': 'As I come to understand that my child-self and my teenage-self are both part of me, ', },
        { 'pillar': 7, 'week': 24, 'content': 'I am becoming aware ', },
        { 'pillar': 7, 'week': 25, 'content': 'Sometimes when I am afraid I ', },
        { 'pillar': 7, 'week': 25, 'content': 'Sometimes when I am hurt I ', },
        { 'pillar': 7, 'week': 25, 'content': 'Sometimes when I am angry I ', },
        { 'pillar': 7, 'week': 25, 'content': 'An effective way to handle fear might be to ', },
        { 'pillar': 7, 'week': 25, 'content': 'An effective way to handle hurt might be to ', },
        { 'pillar': 7, 'week': 25, 'content': 'An effective way to handly anger might be to ', },
        { 'pillar': 7, 'week': 26, 'content': 'Sometimes when I am excited, I ', },
        { 'pillar': 7, 'week': 26, 'content': 'Sometimes when I am turned on sexually, I ', },
        { 'pillar': 7, 'week': 26, 'content': 'Sometimes when I experience strong feelings, I ', },
        { 'pillar': 7, 'week': 26, 'content': 'If I make friends with my excitement, ', },
        { 'pillar': 7, 'week': 26, 'content': 'If I make friends with my sexuality, ', },
        { 'pillar': 7, 'week': 26, 'content': 'As I grow more comfortable with the full range of my emotions, ', },
        { 'pillar': 7, 'week': 27, 'content': 'If I think about becoming better friends with my child-self, ', },
        { 'pillar': 7, 'week': 27, 'content': 'If I think about becoming better friends with my teenage-self, ', },
        { 'pillar': 7, 'week': 27, 'content': 'As my younger selves become more comfortable with me, ', },
        { 'pillar': 7, 'week': 27, 'content': 'As I create a safe space for my child-self, ', },
        { 'pillar': 7, 'week': 27, 'content': 'As I create a safe space for my teenage-self, ', },
        { 'pillar': 7, 'week': 28, 'content': 'Mother gave me a view of myself as ', },
        { 'pillar': 7, 'week': 28, 'content': 'Father gave me a view of myself as ', },
        { 'pillar': 7, 'week': 28, 'content': 'Mother speaks through my voice when I tell myself ', },
        { 'pillar': 7, 'week': 28, 'content': 'Father speaks through my voice when I tell myself ', },
        { 'pillar': 7, 'week': 29, 'content': 'If I bring 5 percent more awareness to my relationship with my mother, ', },
        { 'pillar': 7, 'week': 29, 'content': 'If I bring 5 percent more awareness to my relationship with my father, ', },
        { 'pillar': 7, 'week': 29, 'content': 'If I look at my mother and father realistically, ', },
        { 'pillar': 7, 'week': 29, 'content': 'If I reflect on the level of awareness I bring to my relationship with my mother, ', },
        { 'pillar': 7, 'week': 29, 'content': 'If I reflect on the level of awareness I bring to my relationship with my father, ', },
        { 'pillar': 7, 'week': 30, 'content': 'At the thought of being free of Mother psychologically, ', },
        { 'pillar': 7, 'week': 30, 'content': 'At the thought of being free of Father psychologically, ', },
        { 'pillar': 7, 'week': 30, 'content': 'At the thought of belonging fully to myself, ', },
        { 'pillar': 7, 'week': 30, 'content': 'If my life really does belong to me, ', },
        { 'pillar': 7, 'week': 30, 'content': 'If I really am capable of independent survival, ', },
        { 'pillar': 7, 'week': 31, 'content': 'If I bring 5 percent more awareness to my life, ', },
        { 'pillar': 7, 'week': 31, 'content': 'If I am 5 percent more self-accepting, ', },
        { 'pillar': 7, 'week': 31, 'content': 'If I bring 5 percent more self-responsibility into my life, ', },
        { 'pillar': 7, 'week': 31, 'content': 'If I operate 5 percent more self-assertively, ', },
        { 'pillar': 7, 'week': 31, 'content': 'If I life my life 5 percent more purposefully, ', },
        { 'pillar': 7, 'week': 31, 'content': 'If I bring 5 percent more integrity into my life, ', },
        { 'pillar': 7, 'week': 31, 'content': 'If I breathe deeply and allow myself to experience what self-esteem feels like, ', },
    ]

    for prompt in prompts:
        pillar = None
        week   = None

        if 'pillar' in prompt:
            pillar = Pillar.objects.get(id = prompt['pillar'])

        if 'week' in prompt:
            week = prompt['week']

        p = Prompt.objects.create(
            content = prompt['content'],
            pillar = pillar,
            week = week,
            date = datetime.datetime.now()
        )
        p.save()

if __name__ == '__main__':
    if len(Pillar.objects.all()) < 1:
        create_pillars()

    if len(Prompt.objects.all()) < 1:
        create_prompts()