#!/usr/bin/env python3
"""
CryptoBuddy - A Friendly Crypto Chatbot
A Python-based cryptocurrency recommendation chatbot with personality!
"""

import random

# Predefined crypto database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.greetings = [
            "Hey there! Let's find you a green and growing crypto! 🚀",
            "Welcome to CryptoBuddy! Ready to explore some crypto opportunities? 💰",
            "Hello! I'm here to help you navigate the crypto world! 📈",
            "Greetings, crypto explorer! Let's discover your perfect coin! 🌟"
        ]
        
    def greet(self):
        """Display a friendly greeting"""
        print("=" * 50)
        print(f"🤖 {self.name} - Your Friendly Crypto Assistant 🤖")
        print("=" * 50)
        print(random.choice(self.greetings))
        print("\nI can help you with:")
        print("• Finding trending cryptocurrencies")
        print("• Sustainable crypto recommendations")
        print("• Investment advice based on your goals")
        print("• General crypto information")
        print("-" * 50)
        
    def get_trending_cryptos(self):
        """Find cryptocurrencies with rising price trends"""
        trending = []
        for crypto, data in crypto_db.items():
            if data["price_trend"] == "rising":
                trending.append(crypto)
        return trending
        
    def get_sustainable_cryptos(self):
        """Find environmentally friendly cryptocurrencies"""
        sustainable = []
        for crypto, data in crypto_db.items():
            if data["energy_use"] == "low" and data["sustainability_score"] > 0.7:
                sustainable.append(crypto)
        return sustainable
        
    def get_profitable_advice(self):
        """Recommend crypto for profitability (rising trend + high market cap)"""
        recommendations = []
        for crypto, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                recommendations.append(crypto)
        return recommendations
        
    def get_sustainability_advice(self):
        """Recommend crypto for sustainability (low energy + high sustainability score)"""
        recommendations = []
        for crypto, data in crypto_db.items():
            if data["energy_use"] == "low" and data["sustainability_score"] > 0.7:
                recommendations.append(crypto)
        return recommendations
        
    def get_crypto_info(self, crypto_name):
        """Get detailed information about a specific cryptocurrency"""
        crypto_name = crypto_name.title()  # Capitalize first letter
        if crypto_name in crypto_db:
            data = crypto_db[crypto_name]
            return {
                "name": crypto_name,
                "data": data
            }
        return None
        
    def analyze_query(self, user_input):
        """Analyze user input and provide appropriate response"""
        user_input = user_input.lower()
        
        # Trending/rising queries
        if any(word in user_input for word in ["trending", "rising", "growing", "up", "increase"]):
            trending = self.get_trending_cryptos()
            if trending:
                if len(trending) == 1:
                    response = f"{trending[0]} is currently trending upward! 📈"
                else:
                    response = f"Great choices trending up: {', '.join(trending)}! 🚀"
                return response
            else:
                return "No cryptos are showing strong upward trends right now. Keep watching the market! 👀"
                
        # Sustainability queries
        elif any(word in user_input for word in ["sustainable", "green", "environment", "eco", "clean"]):
            sustainable = self.get_sustainable_cryptos()
            if sustainable:
                crypto = sustainable[0]  # Get the most sustainable
                score = crypto_db[crypto]["sustainability_score"]
                response = f"{crypto} is your best bet for sustainability with a {score:.1f}/10 eco-score! 🌱"
                return response
            else:
                return "For sustainability, I'd recommend looking into proof-of-stake cryptocurrencies! 🌍"
                
        # Long-term/investment queries
        elif any(word in user_input for word in ["long-term", "investment", "future", "growth", "buy", "invest"]):
            profitable = self.get_profitable_advice()
            sustainable = self.get_sustainability_advice()
            
            if sustainable:
                crypto = sustainable[0]
                return f"{crypto} (ADA) is trending up and has a top-tier sustainability score! 🚀"
            elif profitable:
                return f"For long-term growth, consider {profitable[0]} - it's rising with strong market presence! 💎"
            else:
                return "For long-term investment, focus on cryptos with strong fundamentals and rising trends! 📊"
                
        # Specific crypto queries
        elif any(crypto.lower() in user_input for crypto in crypto_db.keys()):
            for crypto in crypto_db.keys():
                if crypto.lower() in user_input:
                    info = self.get_crypto_info(crypto)
                    if info:  # Check if info is not None
                        data = info["data"]
                        trend_emoji = "📈" if data["price_trend"] == "rising" else "➡️"
                        sustainability_emoji = "🌱" if data["sustainability_score"] > 0.6 else "⚡"
                        
                        response = f"{crypto} {trend_emoji}\n"
                        response += f"• Trend: {data['price_trend'].title()}\n"
                        response += f"• Market Cap: {data['market_cap'].title()}\n"
                        response += f"• Energy Use: {data['energy_use'].title()} {sustainability_emoji}\n"
                        response += f"• Sustainability: {data['sustainability_score']:.1f}/10"
                        return response
                    
        # Help/general queries
        elif any(word in user_input for word in ["help", "what", "how", "tell me"]):
            return ("I can help you find:\n"
                   "• Trending cryptos (ask about 'trending' or 'rising')\n"
                   "• Sustainable options (ask about 'green' or 'sustainable')\n"
                   "• Investment advice (ask about 'long-term' or 'investment')\n"
                   "• Specific crypto info (just mention Bitcoin, Ethereum, or Cardano)")
                   
        # Default response
        else:
            responses = [
                "Hmm, I'm not sure about that! Try asking about trending cryptos or sustainability! 🤔",
                "Could you rephrase that? I'm great with questions about crypto trends and green coins! 💚",
                "I didn't quite catch that! Ask me about rising cryptos or eco-friendly options! 🌱"
            ]
            return random.choice(responses)
    
    def add_disclaimer(self):
        """Add investment disclaimer"""
        print("\n" + "⚠️" * 20)
        print("💡 IMPORTANT DISCLAIMER:")
        print("Crypto is risky—always do your own research!")
        print("This is for educational purposes only!")
        print("⚠️" * 20)
        
    def run(self):
        """Main chatbot loop"""
        self.greet()
        
        while True:
            try:
                print(f"\n💬 Ask {self.name} a question (or type 'quit' to exit):")
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print(f"\n{self.name}: Thanks for chatting! Stay crypto-curious! 🚀💰")
                    self.add_disclaimer()
                    break
                    
                if user_input:
                    response = self.analyze_query(user_input)
                    print(f"\n{self.name}: {response}")
                else:
                    print(f"\n{self.name}: I'm here when you're ready to talk crypto! 😊")
                    
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! Keep those investments growing! 🌱")
                self.add_disclaimer()
                break
            except Exception as e:
                print(f"\n{self.name}: Oops! Something went wrong. Let's try again! 🤖")

if __name__ == "__main__":
    # Create and run CryptoBuddy
    buddy = CryptoBuddy()
    buddy.run()