import React from "react";
import { Link, useLocation } from "react-router-dom";
import { createPageUrl } from "@/utils";
import { Heart, Plus, Sparkles, User } from "lucide-react";

export default function Layout({ children, currentPageName }) {
  const location = useLocation();
  
  const navItems = [
    { name: "Home", path: createPageUrl("Home"), icon: Heart },
    { name: "Create", path: createPageUrl("Create"), icon: Plus },
    { name: "My Vision", path: createPageUrl("MyVision"), icon: Sparkles },
  ];

  const isActive = (path) => location.pathname === path;

  return (
    <div className="min-h-screen bg-gradient-to-br from-rose-50 via-purple-50 to-orange-50">
      <style>{`
        :root {
          --gradient-primary: linear-gradient(135deg, #ff6b9d 0%, #c239d3 50%, #ff8c42 100%);
          --gradient-warm: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
          --shadow-glow: 0 8px 32px rgba(255, 107, 157, 0.15);
          --shadow-card: 0 20px 60px rgba(0, 0, 0, 0.08);
        }
        
        body {
          font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        .gradient-text {
          background: var(--gradient-primary);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
        }
        
        .glass-effect {
          background: rgba(255, 255, 255, 0.8);
          backdrop-filter: blur(20px);
          border: 1px solid rgba(255, 255, 255, 0.5);
        }
      `}</style>

      {/* Main Content */}
      <main className="pb-24 min-h-screen">
        {children}
      </main>

      {/* Bottom Navigation */}
      <nav className="fixed bottom-0 left-0 right-0 glass-effect border-t border-white/50 shadow-2xl z-50">
        <div className="max-w-lg mx-auto px-6 py-3">
          <div className="flex justify-around items-center">
            {navItems.map((item) => {
              const Icon = item.icon;
              const active = isActive(item.path);
              
              return (
                <Link
                  key={item.name}
                  to={item.path}
                  className="relative flex flex-col items-center gap-1 transition-all duration-300"
                >
                  <div className={`p-3 rounded-2xl transition-all duration-300 ${
                    active 
                      ? 'bg-gradient-to-r from-pink-500 to-purple-500 shadow-lg shadow-pink-500/50 scale-110' 
                      : 'bg-transparent hover:bg-white/50'
                  }`}>
                    <Icon className={`w-5 h-5 ${active ? 'text-white' : 'text-gray-600'}`} />
                  </div>
                  <span className={`text-xs font-medium ${
                    active ? 'gradient-text font-semibold' : 'text-gray-600'
                  }`}>
                    {item.name}
                  </span>
                </Link>
              );
            })}
          </div>
        </div>
      </nav>
    </div>
  );
}
