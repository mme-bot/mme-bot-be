"""
MME Bot FastAPI Application
Main application entry point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn

from src.config.settings import get_settings

"""비동기 컨텍스트 매니저 데코레이터"""
# @PostConstruct, @PreDestroy
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    print("🚀 Starting MME Bot API...")
    yield
    # Shutdown
    print("🛑 Shutting down MME Bot API...")

# @SpringBootApplication
def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    settings = get_settings() # 환경 설정 객체 로딩
    
    app = FastAPI(
        title="MME Bot API",
        description="A FastAPI application for MME Bot",
        version="1.0.0",
        docs_url="/docs" if settings.DEBUG else None, # swagger
#        redoc_url="/redoc" if settings.DEBUG else None,
        lifespan=lifespan # 앱 생명주기 이벤트 함수 등록
    )
    
    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    # @RestController 로 매핑하는 것
    # app.include_router(users.router, prefix="/api/v1/users", tags=["users"]) # tags -> swagger grouping name
    
    @app.get("/")
    async def root():
        """Root endpoint"""
        return {
            "message": "Welcome to MME Bot API",
            "version": "1.0.0",
            "docs": "/docs" if settings.DEBUG else "Documentation disabled in production"
        }
    
    @app.get("/health")
    async def health_check():
        """Health check endpoint"""
        return {"status": "healthy", "service": "mme-bot-api"}

    # created at 함수가 최종적으로 FastAPI 인스턴스 반환
    return app


# Create the FastAPI app instance
app = create_app() # uvicorn 같은 ASGI 서버가 app 객체를 실행 진입점으로 사용함.

# main 메서드 애플리케이션 진입점.
if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info" if not settings.DEBUG else "debug"
    )
