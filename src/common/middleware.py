from fastapi import Request

class Middleware:      
        
    async def __call__(self, request: Request, call_next):
        response = await call_next(request)
        return response
    
middleware = Middleware()