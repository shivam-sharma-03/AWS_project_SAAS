export default function Card({ children, className }) {
    return (
      <div className={`p-4 bg-gray-800 text-white rounded-md ${className}`}>
        {children}
      </div>
    );
  }
  